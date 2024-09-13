# Use the official Python image.
FROM python:3.9-slim

# Set the working directory.
WORKDIR /app

# Install Celery and Redis.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the Celery tasks.
COPY tasks.py tasks.py

# Run the Celery worker.
CMD ["celery", "-A", "tasks", "worker" ,"--loglevel=info"]

