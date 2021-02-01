from django.db import models


class GeneratedKey(models.Model):
    
    key = models.CharField(verbose_name='Ключ', max_length=255)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Сгенерированный ключ'
        verbose_name_plural = 'Сгенерированные ключи'
    
    def __str__(self):
        return self.key