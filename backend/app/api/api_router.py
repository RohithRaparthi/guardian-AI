from fastapi import APIRouter
from app.api.routes import guardian_routes, event_routes, monitoring_routes, websocket_routes

api_router = APIRouter()

api_router.include_router(guardian_routes.router, prefix="/guardians", tags=["Guardians"])
api_router.include_router(event_routes.router, prefix="/events", tags=["Events"])
api_router.include_router(monitoring_routes.router, prefix="/monitoring", tags=["Monitoring"])
api_router.include_router(websocket_routes.router)
