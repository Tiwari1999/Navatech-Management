from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.admin import Admin
from app.models.requests.admin_request import AdminAuthOrganizationRequest
from app.models.response.admin_response import AdminLoginResponseModel
from app.utils.auth import verify_password, create_jwt_token
from common.db import get_db

router = APIRouter()


@router.post("/login", response_model=AdminLoginResponseModel, summary="Admin login to get JWT token", status_code=200)
async def admin_login(payload: AdminAuthOrganizationRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Admin).filter_by(email=payload.email))
    admin = result.scalars().first()
    if not admin or not verify_password(payload.password, admin.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_jwt_token({"email": admin.email, "org_name": admin.org_name})
    return {"access_token": token, "token_type": "bearer"}
