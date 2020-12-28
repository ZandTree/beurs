# Generated by Django 3.1.3 on 2020-12-26 17:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20201226_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='deleted_at',
            new_name='date_hidden',
        ),
        migrations.AddField(
            model_name='post',
            name='count',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 26, 17, 44, 44, 907513, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
