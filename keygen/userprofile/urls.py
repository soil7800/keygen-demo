from django.urls import path

from .views import github_callback


urlpatterns = [
    path('', github_callback)
]