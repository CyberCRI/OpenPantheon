# OpenPantheon: the pantheon for Education
# Copyright (C) 2021 CRI
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from typing import Any, Dict, List

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/stats", response_model=Dict)
def get_pantheon_stats(db: Session = Depends(deps.get_db), ) -> Any:
    """
    Get stats about the general pantheon.
    """
    return crud.personality.get_stats(db)


@router.get("/", response_model=List[schemas.Personality])
def read_personalities(response: Response,
                       db: Session = Depends(deps.get_db),
                       current_user: models.User = Depends(deps.get_current_active_user),
                       skip: int = 0,
                       limit: int = 100,
                       personal: int = 0,
                       women: bool = False,
                       field: str = '',
                       region: str = '',
                       sort: str = '') -> Any:
    """
    Retrieve personalities.
    """
    count: List[int] = []
    personalities = crud.personality.get_multi_personalities(
        get_count=count,
        db=db,
        current_user_pantheon=current_user.personalities_celebrated,
        skip=skip,
        limit=limit,
        personal=personal,
        women=women,
        field=field,
        region=region,
        sort=sort)
    response.headers["x-total-count"] = str(
        count[0])  # Little hack that takes advantage of list mutability to get count for pagination
    return personalities  # noqa: R504


@router.get("/guest", response_model=List[schemas.Personality])
def read_personalities_guest(response: Response,
                             db: Session = Depends(deps.get_db),
                             skip: int = 0,
                             limit: int = 100,
                             personal: int = 0,
                             women: bool = False,
                             field: str = '',
                             region: str = '',
                             sort: str = '') -> Any:
    """
    Retrieve personalities for unlogged used.
    Necessary because FASTAPI returns 401 if I require current user in function
    """
    count: List[int] = []
    personalities = crud.personality.get_multi_personalities_guest(get_count=count,
                                                                   db=db,
                                                                   skip=skip,
                                                                   limit=limit,
                                                                   women=women,
                                                                   field=field,
                                                                   region=region,
                                                                   sort=sort)
    response.headers["x-total-count"] = str(count[0])
    return personalities  # noqa: R504


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
    return crud.personality.create_new_personality(db=db, obj_in=personality_in)


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
    return crud.personality.update(db=db, db_obj=personality, obj_in=personality_in)


@router.get("/{id}")
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

    for i in range(len(personality.comments)):  # type: ignore
        tab = []
        tmp = personality.comments[i].fluff.split('~')  # type: ignore
        for j in range(len(tmp)):
            tmp_bis = tmp[j].split('|')
            tab.append({'name': tmp_bis[0], 'link': tmp_bis[1]})
        personality.comments[i].fluff = tab  # type: ignore

    return personality


@router.get("/wiki/{wiki_id}", response_model=schemas.Personality)
def read_personality_by_wiki_id(
        *,
        db: Session = Depends(deps.get_db),
        wiki_id: str,
) -> Any:
    """
    Get personality by Wiki ID.
    """
    personality = crud.personality.get_by_wiki(db=db, wiki_id=wiki_id)
    if not personality:
        raise HTTPException(status_code=404, detail="Personality not found")
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
    return crud.personality.remove(db=db, id=id)
