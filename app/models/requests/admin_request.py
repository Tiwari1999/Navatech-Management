from pydantic import BaseModel

# Request model
class AdminAuthOrganizationRequest(BaseModel):
    email: str
    password: str
