from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('generator.urls')),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('login/github_callback/', include('userprofile.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]
