# Generated by Django 4.0 on 2022-11-03 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_appointment_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='created_at',
        ),
    ]