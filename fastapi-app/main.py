from fastapi import FastAPI
from pydantic import BaseModel
from celery import Celery
import os

app = FastAPI()

# Configure Celery.
redis_url = os.getenv('REDIS_URL', 'redis://redis:6379/0')
celery_app = Celery('tasks', broker=redis_url, backend=redis_url)

class TaskModel(BaseModel):
    task: str

@app.post("/enqueue/")
async def enqueue_task(task_model: TaskModel):
    task_id = celery_app.send_task('tasks.process_task', args=[task_model.task])
    return {"task_id": task_id.id}

@app.get("/status/{task_id}")
def task_status(task_id: str):
    task = celery_app.AsyncResult(task_id)
    return {
        "info":task.info,
        "ready":task.ready(),
        "result":task.result,
        "state":task.state}
    """
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'status': 'Task pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'result': task.result
        }
    else:
        response = {
            'state': task.state,
            'status': str(task.info)  # This is the exception raised
        }
    return response
    """

