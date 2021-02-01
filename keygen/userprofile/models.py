from django.db import models
from django.contrib.auth.models import User


class ProfileManager(models.Manager):
    def get_or_create_by_github_id(self, github_user_data):
        try:
            obj = self.get(github_id=github_user_data.get('id'))
        except self.model.DoesNotExist:
            user = User(username=github_user_data.get('login'))
            user.set_unusable_password()
            user.save()
            obj = self.create(
                user=user, 
                avatar_url=github_user_data.get('avatar_url'), 
                github_id=github_user_data.get('id')
            )
        return obj

class Profile(models.Model):
    objects = ProfileManager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_url = models.URLField(null=True)
    github_id = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self):
        return str(self.user)