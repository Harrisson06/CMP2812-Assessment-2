from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.Actions import Actions as ActionsModel

def get_actions(db: Session) -> List[ActionsModel]:
    # Returns all actions from the database.
    return db.query(ActionsModel).all()

def get_action(db: Session, ActionID: int) -> Optional[ActionsModel]:
    # Returns a single action by ActionID, or None if not found.
    return db.query(ActionsModel).filter(ActionsModel.ActionID == ActionID).first()