import enum
import os
import pathlib
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

base_path = pathlib.Path(__file__).parent.parent.resolve()


class Settings(BaseSettings):
    # postgres
    postgres_user: str = os.environ.get("POSTGRES_USER")
    postgres_password: str = os.environ.get("POSTGRES_PASSWORD")
    postgres_host: str = os.environ.get("POSTGRES_HOST")
    postgres_port: int = os.environ.get("POSTGRES_PORT")
    postgres_db: str = os.environ.get("POSTGRES_DB")



@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
