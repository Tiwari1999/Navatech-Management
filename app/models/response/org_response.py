from pydantic import BaseModel


class OrganizationResponseModel(BaseModel):
    name: str
    db_url: str
    admin_email: str

    class Config:
        orm_mode = True


class CreateOrganizationResponseModel(BaseModel):
    message: str
