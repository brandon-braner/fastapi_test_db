from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

user = settings.postgres_user
password = settings.postgres_password
host = settings.postgres_host
port = settings.postgres_port
database = settings.postgres_db

POSTGRES_DB_URL = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(POSTGRES_DB_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def get_db():
    """Get sqlalchemy session."""
    db = SessionLocal()
    return db