from sqlalchemy.orm import Session
from app.models.guardian import Guardian


def create_guardian(db: Session, name: str, email: str):
    guardian = Guardian(name=name, email=email)
    db.add(guardian)
    db.commit()
    db.refresh(guardian)
    return guardian


def get_all_guardians(db: Session):
    return db.query(Guardian).all()
