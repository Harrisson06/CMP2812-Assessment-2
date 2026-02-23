from sqlalchemy import Column, Integer, ForeignKey
from app.db.base import Base

class Notice_actions(Base):
    __tablename__ = "NoticeActions"
    NoticeID = Column(Integer, primary_key=True)
    ActionID = Column(Integer, ForeignKey("Actions.ActionID"))
