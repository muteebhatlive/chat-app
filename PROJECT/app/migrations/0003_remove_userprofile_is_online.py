# Generated by Django 4.2.5 on 2023-09-24 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_online',
        ),
    ]