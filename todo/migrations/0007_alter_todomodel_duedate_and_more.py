# Generated by Django 4.2.16 on 2024-11-21 07:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_vaccinationtodomodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='duedate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='次回投薬'),
        ),
        migrations.AlterField(
            model_name='vaccinationtodomodel',
            name='duedate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='次回予定日'),
        ),
    ]