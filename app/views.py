from django.shortcuts import render,redirect
from . forms import * 
from . models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
	form = RegisterForm()
	if request.method == 'POST':
		form= RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = RegisterForm()

	context = {"form":form}

	return render (request,'register.html',context)

def loginpage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('lecturerpage')
		

	context = {}
	return render(request, 'login.html', context)

def logoutpage(request):
	logout(request)
	return redirect('login')


def create_appointments_page(request):
	form = AppointmentForm()
	context = {'form':form}
	if request.method == 'POST':
		form = AppointmentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

	return render(request,'createappointment.html',context)


def homepage(request):
	if 'q' in request.GET:
		q= request.GET['q']
		appointments = Appointment.objects.filter(student_reg__icontains=q )
		appointments = Appointment.objects.filter(student_full_name__icontains=q)
	else:
		
		appointments = Appointment.objects.all()
	context = {"appointments":appointments}

	return render(request,'home.html',context)

@login_required(login_url='login')
def lecturerpage(request):
	if 'q' in request.GET:
		q= request.GET['q']
		appointments = Appointment.objects.filter(lecturer_full_name__icontains=q )
	else:
		
		appointments = Appointment.objects.all()
	context = {"appointments":appointments}

	return render(request,'lecturerpage.html',context)

@login_required(login_url='login')
def respondpage(request,pk):
	appointments = Appointment.objects.get(id=pk)
	form = AppointmentForm(instance=appointments)
	if request.method == 'POST':
		form = AppointmentForm(request.POST,instance=appointments)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'form':form}

	return render (request,"respond.html",context)

@login_required(login_url='login')
def deletepage(request,pk):
	appointments  = Appointment.objects.get(id=pk)
	
	if request.method == 'POST':
		appointments.delete()
		return redirect('lecturerpage')
	context = {'appointments':appointments}



	return render(request,"delete.html",context)