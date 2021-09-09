from typing import Any
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.api import deps
from app.models.user import User

router = APIRouter()

@router.get("/live/", status_code=200)
def live_check(
) -> Any:
    """
    Kubernetes Live Check
    """
    return

@router.get("/ready/", status_code=200)
def ready_check(
	db: Session = Depends(deps.get_db),
) -> Any:
    """
    Kubernetes Ready Check
    """
    db.execute("SELECT 1")
    return
