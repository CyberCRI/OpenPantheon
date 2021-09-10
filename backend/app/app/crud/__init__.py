from .crud_comment import comment
from .crud_personality import personality
from .crud_user import user

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.personality import Personality
# from app.schemas.personality import PersonalityCreate, PersonalityUpdate

# personality = CRUDBase[Personality, PersonalityCreate, PersonalityUpdate](Personality)
