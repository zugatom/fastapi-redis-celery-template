# fastapi-redis-celery-template

This took me some hours to make it work, so I guess it could help others ! Enjoy ^^

This repo provides the docker-compose.yml file allowing to build an architecture containing : 
- a FastAPI app : this aims at being the backend of your app.
- a Redis instance : message broker.
- a Celery worker : instance that will perform heavy background tasks.
- a Celery Monitoring Tool called Flower : web page providing real time info on the celery worker.

# How to launch the project ?  
`> docker-compose up --build `

# How to make it work ? 
1. Post a request to FastAPI App : 

> curl -X POST http://localhost:8000/enqueue/ \
    -H "Content-Type: application/json" \
    -d '{"task": "sample task"}'

This command returns for example : 
{"task_id":"ea8c4fdf-ef99-4dbe-b6fc-776231758e35"}

2. Let the celery worker process it without impacting the FastAPI app performance.

3. Monitor the task via Flower (localhost:5555)

OR using : 
> curl -X GET http://localhost:8000/status/{task_id}

Ex : 
curl -X GET http://localhost:8000/status/ea8c4fdf-ef99-4dbe-b6fc-776231758e35