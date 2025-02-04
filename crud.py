from sqlalchemy.orm import Session
from models import CleanedData

def get_data(db: Session, skip: int = 0, limit: int = 10):
    return db.query(CleanedData).offset(skip).limit(limit).all()
