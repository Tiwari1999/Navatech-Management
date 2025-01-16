from fastapi import FastAPI

from common.db import Base, engine, init_db
from config import settings
from router import api_router


# Include routers
def get_fastapi_application() -> FastAPI:
    server = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        docs_url="/docs",
        openapi_url="/schema-pc/openapi.json"
    )

    server.include_router(api_router)

    # Remove the sync table creation
    # Base.metadata.create_all(bind=engine)  <- Remove this line
    return server


application_server = get_fastapi_application()

# Add this to handle async table creation on startup
@application_server.on_event("startup")
async def on_startup():
    await init_db()
