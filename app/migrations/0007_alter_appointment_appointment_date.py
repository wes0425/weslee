# Generated by Django 4.0 on 2022-11-02 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_appointment_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateField(),
        ),
    ]