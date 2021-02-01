import random

from celery import shared_task

from .models import GeneratedKey

@shared_task
def update_key():
    new_key = random.randrange(100000, 999999, 1)
    try:
        obj = GeneratedKey.objects.get(id=1)
    except GeneratedKey.DoesNotExist:
        obj = GeneratedKey(id=1)
    obj.key = str(new_key)
    obj.save()
   