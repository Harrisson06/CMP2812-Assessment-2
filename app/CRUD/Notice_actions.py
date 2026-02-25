from sqlalchemy.orm import Session
from app.models.Notice_actions import Notice_actions as Notice_actions_model

def get_notice_actions(db: Session):
    # Returns all Correction notices 
    return db.query(Notice_actions_model).all()

def get_notice_action(db: Session, NoticeID: int):
    # Returns a specific notice relating to the notice ID
    return db.query(Notice_actions_model).filter(Notice_actions_model.NoticeID == NoticeID).first()