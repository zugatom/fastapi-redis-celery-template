from celery import Celery
import os

# Create a Celery instance.
app = Celery('tasks', 
             broker=os.getenv('REDIS_URL', 'redis://redis:6379/0'),
             backend=os.getenv('REDIS_URL', 'redis://redis:6379/0'))

