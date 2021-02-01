from django.apps import AppConfig
from django.db.models.signals import post_save


class GeneratorConfig(AppConfig):
    name = 'generator'
    
    def ready(self):
        from .signals import change_key
        post_save.connect(change_key, sender='generator.GeneratedKey')