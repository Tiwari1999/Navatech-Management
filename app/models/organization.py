from sqlalchemy import Column, Integer, String

from app.models.base import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    db_url = Column(String, nullable=False)
    admin_email = Column(String, nullable=False)
