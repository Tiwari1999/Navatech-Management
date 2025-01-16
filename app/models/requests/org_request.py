from pydantic import BaseModel

# Request model
class CreateOrganizationRequest(BaseModel):
    admin_email: str
    password: str
    organization_name: str
