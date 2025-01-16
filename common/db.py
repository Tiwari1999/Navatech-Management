from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import asyncio

from config import settings

# Use create_async_engine for async support
engine = create_async_engine(settings.DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

# Async session dependency
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Add this function for async table creation
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
