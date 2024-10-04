# Generated by Django 4.0 on 2022-11-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_appointment_appointment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='statuses',
            field=models.CharField(choices=[('pending', 'pending'), ('approved', 'approved'), ('rejected', 'rejected')], default='pending', max_length=300),
        ),
    ]