# Generated by Django 4.0 on 2022-10-31 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_appointment_delete_apply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.CharField(choices=[('10:00 A.M', '10:00 A.M'), ('10:30 A.M', '10:30 A.M'), ('11:00 A.M', '11:00 A.M'), ('11:30 A.M', '11:30 A.M'), ('12:00 P.M', '12:00 P.M'), ('12:30 P.M', '12:30 P.M'), ('01:00 P.M', '01:00 P.M'), ('01:30 P.M', '01:30 P.M'), ('05:00 P.M', '05:00 P.M'), ('05:30 P.M', '05:30 P.M'), ('06:00 P.M', '06:00 P.M'), ('06:30 P.M', '06:30 P.M'), ('07:00 P.M', '07:00 P.M'), ('07:30 P.M', '07:30 P.M'), ('08:00 P.M', '08:00 P.M'), ('08:30 P.M', '08:30 P.M')], default='', max_length=10),
        ),
    ]