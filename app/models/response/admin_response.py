from pydantic import BaseModel


class AdminLoginResponseModel(BaseModel):
    access_token: str
    token_type: str
