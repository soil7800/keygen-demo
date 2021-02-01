from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import GeneratedKey

@login_required()
def index(request):
    key = GeneratedKey.objects.get(id=1)
    key_updated = int(key.updated.timestamp()*1000)
    return render(request, 'index.html', context={'key': key, 'update_timestamp': key_updated})