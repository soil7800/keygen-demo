from django.contrib.auth import login
from django.shortcuts import render, redirect

from .models import Profile
from .utils import get_github_access_token, get_github_user_data


def github_callback(request):
    github_code = request.GET.get('code', None)
    if github_code:
        github_access_token = get_github_access_token(github_code)
        github_user_data = get_github_user_data(github_access_token)
        user = Profile.objects.get_or_create_by_github_id(github_user_data).user
        login(request, user)
    return redirect('/')