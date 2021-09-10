from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.personality import PersonalityCreate
from app.tests.utils.utils import random_lower_string


def create_random_personality(db: Session) -> models.Personality:
    name = random_lower_string()
    description = random_lower_string()
    personality_in = PersonalityCreate(name=name, description=description, id=id)
    return crud.personality.create_new_personality(db=db, obj_in=personality_in)
