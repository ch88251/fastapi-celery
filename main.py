import os
from celery import Celery
from fastapi import FastAPI

api = FastAPI()

celery = Celery(
    __name__,
    broker=os.environ.get("CELERY_BROKER_URL") or "redis://127.0.0.1:6379/0",
    backend=os.environ.get("CELERY_BROKER_URL") or "redis://127.0.0.1:6379/0"
)

@api.get("/")
def read_root():
    return {"Hello": "World"}

@celery.task
def divide(x, y):
    import time
    time.sleep(5)
    return x / y