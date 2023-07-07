from django.views.generic import TemplateView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404,redirect
from admins.models import Appointment
from admins.forms import AppointmentForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Profile
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.core.mail import send_mail
from django.conf import settings




def quick_appointmnet(request):
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string
	print(group_name)
	if "User" == group_name:
		user_name=request.user.get_username()
		appointment_list = Appointment.objects.all().order_by("-user")
		q=request.GET.get("q")#search start
		if q:
			appointment_list=appointment_list.filter(user__first_name__icontains=q)
		else:
			appointment_list = appointment_list# search end

		available_appointments = []

		for appointment in appointment_list:
			users = appointment.appointment_with.split(',')
			print(users)
			print(user_name)
			if not user_name in users:
				available_appointments.append(appointment)

		appointments= {
		    "query": available_appointments,
		    "user_name":user_name
		}
		return render(request, 'user_quick_appointmnet.html', appointments )
	else:
		return redirect('/')


def user(request):#this section for my appointment
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string
	if "User" == group_name:
		user_name=request.user.get_username()#Getting Username
		#Getting all Post and Filter By Logged UserName
		appointment_list = Appointment.objects.all()

		available_appointments = []
		for appointment in appointment_list:
			users = appointment.appointment_with.split(',')
			print(users)
			print(user_name)
			if user_name in users:
				available_appointments.append(appointment)
		q=request.GET.get("q")#search start
		if q:
			available_appointments=appointment_list.filter(user__first_name__icontains=q)
		else:
			available_appointments = available_appointments
		

		appointments= {
		    "query": available_appointments,
		    "user_name":user_name,    
		}
		print(request.user.email)
		return render(request, 'user.html', appointments )
	else:
		return redirect('/')

def appointment_book(request, id):#activate after clicking book now button
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string
	user = request.user
	profile, created = Profile.objects.get_or_create(user=user)
	if "User" == group_name:
		single_appointment= Appointment.objects.get(id=id)
		single_appointment.booked_count = single_appointment.booked_count+1
		single_appointment.save()
		if request.method == "POST":
			name = request.POST.get('name')
			email = request.POST.get('email')
			phno = request.POST.get('phno')
			print(name)
			print(email)
			print(phno)
			user.first_name = name
			user.email = email
			user.save()
			profile.phone_number = phno
			profile.save()
		user_name=request.user.get_username()
		form = single_appointment
		if form.appointment_with == '':
			form.appointment_with=user_name
		else:
			form.appointment_with= form.appointment_with+','+user_name		
		form.save()
		#return HttpResponseRedirect (instance.get_absolute_url())
		#messages.success(request, 'Your profile was updated.')
		return redirect('/user/')
	else:
		return redirect('/')
	
def appointment_book_check(request, id):
	book_id = id
	return render(request, 'check.html', {"id":book_id})

from django.contrib.auth.models import User

def signup(request):
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		phno = request.POST.get("phno")
		id = request.POST.get("id")
		password = request.POST.get("password")

		user = User.objects.create_user(username=name, email=email, password=password)
		user.save()
		profile, created = Profile.objects.get_or_create(user=user)
		profile.id = id
		profile.phone_number = phno
		profile.save()
		messages.success(request, "Your account has been successfully created.")
		return redirect("/")
    
	return render(request, 'user_signup.html')






