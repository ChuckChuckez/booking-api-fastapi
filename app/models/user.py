from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from db.database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String) # Estaria guay volver luego y hacer cosas de hashear