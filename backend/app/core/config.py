from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "NeuroFold"
    ENVIRONMENT: str = "development"

    # Redis (for Celery)
    REDIS_URL: str = "redis://redis:6379/0"

    class Config:
        env_file = ".env"

settings = Settings()
