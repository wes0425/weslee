from django.db import models

# Create your models here.

departments=(
	("Science and Technology","Science and Technology"),
	("Commercials","Commercials"),
	("Arts","Arts"),
	("Medicine","Medicine"),
	("Law","Law"),


	)
Time = [
	("06:00 A.M","06:00 A.M"),
    ("06:30 A.M","06:30 A.M"),
    ("07:00 A.M","07:00 A.M"),
    ("07:30 A.M","07:30 A.M"),
    ("08:00 A.M","08:00 A.M"),
    ("08:30 A.M","08:30 A.M"),
    ("10:00 A.M","10:00 A.M"),
    ("10:30 A.M","10:30 A.M"),
    ("11:00 A.M","11:00 A.M"),
    ("11:30 A.M","11:30 A.M"),
    ("12:00 P.M","12:00 P.M"),
    ("12:30 P.M","12:30 P.M"),
    ("01:00 P.M","01:00 P.M"),
    ("01:30 P.M","01:30 P.M"),
    ("05:00 P.M","05:00 P.M"),
    ("05:30 P.M","05:30 P.M"),

]
status =(
	("pending...","pending..."),
	("approved","approved"),
	("rejected","rejected"),

	)
duration=(
	("5mins","5mins"),
	("10mins","10mins"),
	("15mins","15mins"),
	("20mins","20mins"),
	("25mins","25mins"),
	("30mins","35mins"),
	("45mins","45mins"),
	("1hour","1hour"),
	
	)

day = (
	("Monday","Monday"),
	("Tuesday","Tuesday"),
	("Wednesday","Wednesday"),
	("Thursday","Thursday"),
	("Friday","Friday"),

	
	)
class Appointment(models.Model):
	lecturer_full_name = models.CharField(max_length=300)
	department = models.CharField(max_length=300,choices=departments)
	student_full_name= models.CharField(max_length=300)
	student_reg= models.CharField(max_length=300)
	student_email = models.EmailField(max_length=300)
	appointment_day = models.CharField(max_length=300,choices=day,default='')
	appointment_time = models.CharField(max_length=10, choices=Time,default="")
	duration = models.CharField(max_length=300,choices=duration)
	aim = models.CharField(max_length=300)
	phonenumber = models.CharField(max_length=300)
	statuses = models.CharField(max_length=300,choices=status,default="pending...")


	
	def __str__(self):

		return self.lecturer_full_name

