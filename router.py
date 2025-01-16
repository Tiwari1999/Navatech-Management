from fastapi import APIRouter

from app.routers import org, admin

api_router = APIRouter(prefix="/v1")

api_router.include_router(org.router, prefix="/org", tags=["Organization"])
api_router.include_router(admin.router, prefix="/admin", tags=["Admin"])
