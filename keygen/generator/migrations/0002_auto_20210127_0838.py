# Generated by Django 3.1.5 on 2021-01-27 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generatedkey',
            name='key',
            field=models.CharField(max_length=255, verbose_name='Ключ'),
        ),
    ]