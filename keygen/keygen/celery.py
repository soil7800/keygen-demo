import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "keygen.settings")
app = Celery("keygen")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

@app.task(name='debug-task')
def debug_task():
    print('success')