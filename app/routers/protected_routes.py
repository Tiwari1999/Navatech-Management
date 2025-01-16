from fastapi import APIRouter, Depends

from common.auth_middleware import auth_required

router = APIRouter()


@router.get("/protected-endpoint")
async def protected_endpoint(auth_data: dict = Depends(auth_required)):
    # auth_data contains {"email": "user@example.com", "org_name": "org_name"}
    return {"message": f"Hello {auth_data['email']} from {auth_data['org_name']}"}


@router.get("/public-endpoint")
async def public_endpoint():
    # No auth required
    return {"message": "This is public"}
