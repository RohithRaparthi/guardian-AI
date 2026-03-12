from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import cv2
from pydantic import BaseModel

from app.services.pose_service import detect_pose
from app.services import monitoring_state

router = APIRouter()

cap = cv2.VideoCapture(0)


def generate_frames():
    while True:
        success, frame = cap.read()

        if not success:
            continue

        frame, _ = detect_pose(frame)

        ret, buffer = cv2.imencode(".jpg", frame)
        frame_bytes = buffer.tobytes()

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + frame_bytes
            + b"\r\n"
        )


@router.get("/video-feed")
def video_feed():
    return StreamingResponse(
        generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )


@router.get("/status")
def get_status():
    return {
        "posture": monitoring_state.posture_status,
        "fall_detected": monitoring_state.fall_detected,
        "last_fall_time": monitoring_state.last_fall_time
    }


class GuardianSelect(BaseModel):
    email: str


@router.post("/select-guardian")
def select_guardian(data: GuardianSelect):
    monitoring_state.selected_guardian_email = data.email
    return {"message": "Guardian selected"}