# Generated by Django 4.0.6 on 2024-03-18 22:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0003_remove_album_banda_remove_album_datadecriacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='datadecriacao',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
