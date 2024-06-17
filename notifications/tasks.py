import time
from celery import shared_task
import time


@shared_task(queue='tasks')
def send_sms_to_user():
    time.sleep(5)
    return
