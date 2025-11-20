from backend.app.workers.celery_worker import celery

@celery.task(name="tasks.example")
def example_task():
    return "Task executed!"