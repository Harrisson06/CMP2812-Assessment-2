from pydantic import BaseModel

# Base schema for the Notice_actions table
class NoticeActionsBase(BaseModel):
    NoticeID: int
    ActionID: int

# Full schema for Notice_actions, allows orm mapping from the db models. 
class NoticeActions(NoticeActionsBase):
    class Config:
        from_attributes = True