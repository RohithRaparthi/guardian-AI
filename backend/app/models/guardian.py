from sqlalchemy import Column, Integer, String
from app.database.base import Base   # ✅ FIXED HERE


class Guardian(Base):
    __tablename__ = "guardians"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)