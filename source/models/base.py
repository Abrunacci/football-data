from os import environ

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

DB_USER = environ.get('POSTGRES_USER')
DB_NAME = environ.get('POSTGRES_NAME')
DB_PASS = environ.get('POSTGRES_PASS')
DB_PORT = int(environ.get('POSTGRES_PORT'))
DB_HOST = environ.get('POSTGRES_HOST')

engine = create_engine(
    f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class BaseDBModel(Base):
    """Base model class representation."""
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True)