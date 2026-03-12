from fastapi import APIRouter, WebSocket
import asyncio
from app.services import monitoring_state

router = APIRouter()


@router.websocket("/ws/alerts")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        await asyncio.sleep(1)
        if monitoring_state.fall_detected:
            await websocket.send_json({
                "event": "FALL_DETECTED"
            })
