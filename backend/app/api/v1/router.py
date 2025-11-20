from fastapi import APIRouter
from .celery_test import router as celery_test_router

router = APIRouter()

router.include_router(
    celery_test_router,
    prefix="/tasks",
    tags=["Tasks"]
)
