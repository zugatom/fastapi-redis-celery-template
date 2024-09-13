# Use the official Python image.
FROM python:3.9-slim

# Set the working directory.
WORKDIR /app

# Install FastAPI, Uvicorn, Celery, and Redis.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the FastAPI app.
COPY main.py main.py

# Expose port 8000.
EXPOSE 8000

# Run the FastAPI app.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

