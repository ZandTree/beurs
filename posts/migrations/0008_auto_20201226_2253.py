# Generated by Django 3.1.3 on 2020-12-26 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]