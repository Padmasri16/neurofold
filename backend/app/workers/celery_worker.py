from celery import Celery
from backend.app.core.config import settings

celery = Celery(
    "neurofold",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=["backend.app.core.tasks"],
)

@celery.task(name="test.ping")
def ping():
    return "pong"
