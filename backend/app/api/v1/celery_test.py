from fastapi import APIRouter
from backend.app.workers.celery_worker import ping

router = APIRouter()

@router.get("/test-celery")
def test_celery():
    task = ping.delay()
    return {"message": "Task sent to Celery", "task_id": task.id}
