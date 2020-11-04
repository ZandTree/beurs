# Generated by Django 3.1.2 on 2020-11-04 18:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='customer',
            name='add_phone_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customer',
            name='designation',
            field=models.CharField(default=True, max_length=120),
        ),
        migrations.AddField(
            model_name='customer',
            name='location',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='add_phone_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(default=True, max_length=120),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]