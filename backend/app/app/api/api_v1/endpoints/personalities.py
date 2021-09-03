from typing import Any, List, Dict

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/stats", response_model=Dict)
def get_pantheon_stats(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get stats about the general pantheon.
    """
    stats = crud.personality.get_stats(db)
    return stats

@router.get("/", response_model=List[schemas.Personality])
def read_personalities(
	response: Response,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    skip: int = 0,
    limit: int = 100,
    personal: int = 0,
    women: bool = False,
    field: int = 0,
    sort: str = ''
) -> Any:
    """
    Retrieve personalities.
    """
    count = []
    personalities = crud.personality.get_multi_personalities(get_count=count, db=db, current_user_pantheon=current_user.personalities_celebrated, skip=skip, limit=limit, personal=personal, women=women, field=field, sort=sort)
    response.headers["x-total-count"] = str(count[0]) # Little hack that takes advantage of list mutability to get count for pagination
    return personalities

@router.get("/guest", response_model=List[schemas.Personality])
def read_personalities_guest(
    response: Response,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    personal: int = 0,
    women: bool = False,
    field: int = 0,
    sort: str = ''
) -> Any:
    """
    Retrieve personalities for unlogged used. Necessary because FASTAPI returns 401 if I require current user in function
    """
    count = []
    personalities = crud.personality.get_multi_personalities_guest(get_count=count, db=db, skip=skip, limit=limit, women=women, field=field, sort=sort)
    response.headers["x-total-count"] = str(count[0])
    return personalities

@router.post("/", response_model=schemas.Personality)
def create_personality(
    *,
    db: Session = Depends(deps.get_db),
    personality_in: schemas.PersonalityCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new personality.
    """
    personality = crud.personality.create_new_personality(db=db, obj_in=personality_in)
    return personality


@router.put("/{id}", response_model=schemas.Personality)
def update_personality(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    personality_in: schemas.PersonalityUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an personality.
    """
    personality = crud.personality.get(db=db, id=id)
    if not personality:
        raise HTTPException(status_code=404, detail="Personality not found")
    # if not crud.user.is_superuser(current_user) and (personality.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    personality = crud.personality.update(db=db, db_obj=personality, obj_in=personality_in)
    return personality


@router.get("/{id}", response_model=schemas.Personality)
def read_personality(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get personality by ID.
    """
    personality = crud.personality.get(db=db, id=id)
    if not personality:
        raise HTTPException(status_code=404, detail="Personality not found")
    return personality

@router.get("/wiki/{wiki_id}", response_model=schemas.Personality)
def read_personality(
    *,
    db: Session = Depends(deps.get_db),
    wiki_id: str,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get personality by Wiki ID.
    """
    personality = crud.personality.get_by_wiki(db=db, wiki_id=wiki_id)
    if not personality:
        raise HTTPException(status_code=404, detail="Personality not found")
    # if not crud.user.is_superuser(current_user) and (personality.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    return personality

@router.delete("/{id}", response_model=schemas.Personality)
def delete_personality(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an personality.
    """
    personality = crud.personality.get(db=db, id=id)
    if not personality:
        raise HTTPException(status_code=404, detail="Personality not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    personality = crud.personality.remove(db=db, id=id)
    return personality
