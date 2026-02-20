from pydantic import BaseModel
from typing import Optional

# Base schema for the Actions table
class ActionsBase(BaseModel):
    Actions_desc: Optional[int] = None

# Full schema for Actions, allows orm mapping from the db models. 
class Actions(ActionsBase):
    ActionID: int
    class config:
        from_attributes = True
