from celery import Celery
from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')

app = Celery('celery_project')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
@app.task
def send_notifications():
    pass