# Generated by Django 4.0.6 on 2024-03-19 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='post',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='comment',
            field=models.TextField(),
        ),
    ]
