from pydantic_settings import BaseSettings


class Application(BaseSettings):
    """"""

    RUN_ENV: str
    DEBUG: bool
    PROJECT_NAME: str
    SECRET_KEY: str
    ALGORITHM: str
    DATABASE_URL: str

    class Config:
        """"""
        env_file = "local.env"
        case_sensitive = True


settings: Application = Application()
