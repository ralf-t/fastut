from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from core.config import settings

# SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# uncomment above if u want to use pgsql then comment these two lines below
SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

# the actual db sessionw
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()