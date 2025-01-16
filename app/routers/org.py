from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.models.admin import Admin
from app.models.organization import Organization
from app.models.requests.org_request import CreateOrganizationRequest
from app.models.response.org_response import CreateOrganizationResponseModel, OrganizationResponseModel
from app.utils.auth import hash_password
from common.db import get_db

router = APIRouter()


@router.post("/create", response_model=CreateOrganizationResponseModel, summary="Create a new organization with an admin user", status_code=200)
async def create_organization(payload: CreateOrganizationRequest, db: AsyncSession = Depends(get_db)):
    try:
        # Check if organization exists
        result = await db.execute(select(Organization).filter_by(name=payload.organization_name))
        org = result.scalars().first()
        if org:
            raise HTTPException(status_code=400, detail="Organization already exists")

        # Create only the organization if admin exists
        new_org = Organization(
            name=payload.organization_name, 
            db_url=f"sqlite:///{payload.organization_name}.sqlite3", 
            admin_email=payload.admin_email
        )
        db.add(new_org)

        # Check if admin exists
        admin_result = await db.execute(select(Admin).filter_by(email=payload.admin_email))
        admin = admin_result.scalars().first()
        
        # Only create admin if it doesn't exist
        if not admin:
            hashed_password = hash_password(payload.password)
            new_admin = Admin(
                email=payload.admin_email, 
                password=hashed_password, 
                org_name=payload.organization_name
            )
            db.add(new_admin)

        await db.commit()
        return {"message": "Organization created successfully"}

    except HTTPException as he:
        raise he
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/get", response_model=OrganizationResponseModel, summary="Retrieve organization details by name",
            status_code=200)
async def get_organization(organization_name: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Organization).filter_by(name=organization_name))
    org = result.scalar_one_or_none()
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org
