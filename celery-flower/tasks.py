from celery import Celery
import os

# Create a Celery instance.
app = Celery('tasks', 
             broker=os.getenv('REDIS_URL', 'redis://redis:6379/0'),
             backend=os.getenv('REDIS_URL', 'redis://redis:6379/0'))

@app.task(name='tasks.process_task')
def process_task(task):
    import time
    for i in range(0,20):
        print("processing...", flush=True)
        time.sleep(1)  # Simulate a long-running task
    return f"Processed task: {task}"

