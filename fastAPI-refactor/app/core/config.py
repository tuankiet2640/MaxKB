# Core configuration settings for FastAPI

from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI DDD Project"
    debug: bool = True
    database_url: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"

settings = Settings()
