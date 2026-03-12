from sqlalchemy.orm import Session
from app.models.fall_event import FallEvent


def create_event(db: Session, guardian_id: int, confidence: float):
    event = FallEvent(
        guardian_id=guardian_id,
        event_type="FALL",
        confidence=confidence
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


def get_events(db: Session):
    return db.query(FallEvent).all()
