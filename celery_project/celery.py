import time

from celery import Celery
from django.conf import settings
from kombu import Exchange, Queue
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')

app = Celery('celery_project')
app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks()

app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
]
app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1


@app.task
def send_notifications():
    pass


@app.task(queue='tasks')
def task1():
    time.sleep(3)
    return


@app.task(queue='tasks')
def task2():
    time.sleep(3)
    return


@app.task(queue='tasks')
def task3():
    time.sleep(3)
    return


@app.task(queue='tasks')
def task4():
    time.sleep(3)
    return


def handle_tasks():
    task2.apply_async(priorety=1)
    task4.apply_async(priorety=1)
    task2.apply_async(priorety=3)
    task3.apply_async(priorety=2)
    task1.apply_async(priorety=4)
    task3.apply_async(priorety=4)
    task1.apply_async(priorety=2)
    task4.apply_async(priorety=3)

