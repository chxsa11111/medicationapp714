# Generated by Django 5.1 on 2024-10-27 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todomodel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='todomodel',
            name='update_at',
        ),
    ]