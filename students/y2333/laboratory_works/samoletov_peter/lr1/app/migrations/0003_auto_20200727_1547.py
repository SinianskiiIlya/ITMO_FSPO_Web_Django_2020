# Generated by Django 3.0.8 on 2020-07-27 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200727_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='book',
        ),
        migrations.AddField(
            model_name='card',
            name='book',
            field=models.IntegerField(default=None),
        ),
        migrations.RemoveField(
            model_name='card',
            name='reader',
        ),
        migrations.AddField(
            model_name='card',
            name='reader',
            field=models.IntegerField(default=None),
        ),
    ]