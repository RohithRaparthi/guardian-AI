from pydantic import BaseModel
from datetime import datetime


class EventResponse(BaseModel):
    id: int
    guardian_id: int
    event_type: str
    confidence: float
    created_at: datetime

    model_config = {"from_attributes": True}
