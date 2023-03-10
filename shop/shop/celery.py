import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')

app = Celery('celery_hm', broker='amqp://localhost')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sync_orders': {
        'task': 'orders.tasks.sync_orders',
        'schedule': crontab(minute=0)
    },
    'sync_book': {
        'task': 'orders.tasks.sync_book',
        'schedule': crontab(minute=0)
    }

}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
