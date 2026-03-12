from sqlalchemy.orm import Session
from app.crud.event_crud import create_event
from app.models.guardian import Guardian
from app.services.email_service import send_email
from app.services.sound_service import play_alarm
from app.core.constants import FALL_CONFIDENCE_DEFAULT, ALERT_COOLDOWN_SECONDS
from app.utils.helpers import can_trigger_alert
from app.utils.logger import logger


def trigger_alert(db: Session):
    if not can_trigger_alert(ALERT_COOLDOWN_SECONDS):
        return

    guardians = db.query(Guardian).all()

    for guardian in guardians:
        create_event(db, guardian.id, FALL_CONFIDENCE_DEFAULT)
        send_email(guardian.email)

    play_alarm()
    logger.info("Fall alert triggered")
