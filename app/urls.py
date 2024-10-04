from django.urls import path
from . import views 

urlpatterns = [

	path('register/',views.register,name="register"),
	path('login/',views.loginpage,name="login"),
	path('logout/',views.logoutpage,name="logout"),
	path('delete/<str:pk>/',views.deletepage,name="delete"),
	path('',views.homepage,name="home"),
	path('lecturerpage/',views.lecturerpage,name="lecturerpage"),
	path('create_appointments/',views.create_appointments_page,name="create_appointments_page"),
	path('respond/<str:pk>/',views.respondpage,name="respond"),
]
