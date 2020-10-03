from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Boolean, DateTime


Base = declarative_base()


class BaseModel(Base):
    """Base model class representation."""
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True)