from django.conf import settings
from django.contrib.auth.models import User
import requests


def get_github_access_token(code):
    data = {
        'client_id': settings.GITHUB_CLIENT_ID,
        'client_secret': settings.GITHUB_CLIENT_SECRET,
        'code': code,
    }
    headers = {
        'Accept': 'application/json',
    }
    request = requests.post(
        'https://github.com/login/oauth/access_token', 
        headers=headers, 
        data=data
    )
    access_token = request.json().get('access_token')
    return access_token

def get_github_user_data(token):
    headers = {
        'Authorization': f'token {token}',
    }
    request = requests.get('https://api.github.com/user', headers=headers)
    user_data = request.json()
    return user_data