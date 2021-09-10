from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps

router = APIRouter()


@router.get("/live/", status_code=200)
def live_check() -> Any:
    """
    Kubernetes Live Check
    """
    return


@router.get("/ready/", status_code=200)
def ready_check(db: Session = Depends(deps.get_db), ) -> Any:
    """
    Kubernetes Ready Check
    """
    db.execute("SELECT 1")
    return
