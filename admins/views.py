from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404,redirect
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def edit_users(request, id):
	slot = Appointment.objects.get(id=id)
	studs = slot.appointments_with()
	studs = studs.split(',')
	if studs[0] == '':
		studs = None
	return render(request, 'view_users.html', {"users":studs, "slot":slot} )
	
def delete_users(request):
    user = request.POST.get('user')
    id = request.POST.get('id')
    slot = get_object_or_404(Appointment, id=id)
    users = slot.appointments_with().split(',')

    if user in users:
        users.remove(user)

    # Check if the list is empty or has users
    if users:
        result = ', '.join(users)
    else:
        result = ''  # Set the result to an empty string

    slot.appointment_with = result
    slot.save()

    return JsonResponse({'message': 'user deleted successfully'})

	


def admin(request):#this section for my appointment
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string
	if "Admin" == group_name:
		user_name=request.user.get_username()#Getting Username

		#Getting all Post and Filter By Logged UserName
		appointment_list = Appointment.objects.all().order_by("-id").filter(user=request.user)
		q=request.GET.get("q")#search start
		if q:
			appointment_list=appointment_list.filter(appointment_with__icontains=q)
		else:
			appointment_list = appointment_list# search end

		appointments= {
		    "query": appointment_list,
		    "user_name":user_name,
		}
		return render(request, 'admin.html', appointments )
	else:
		return redirect('/') 

def admin_appointment_list(request):
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string
	if "Admin" == group_name:
		user_name=request.user.get_username()#Getting Username

		#Getting all Post and Filter By Logged UserName
		appointment_list = Appointment.objects.all().order_by("-id").filter(user=request.user)
		q=request.GET.get("q") #search start
		if q:
			appointment_list=appointment_list.filter(date__icontains=q)
		else:
			appointment_list = appointment_list #search end

		appointments= {
		    "query": appointment_list,
		    "user_name":user_name,
		    "form":AppointmentForm(),
		}
		form = AppointmentForm(request.POST or None)
		if form.is_valid():
			saving=form.save(commit=False)
			saving.user=request.user
			print("hello")
			print("hi",request.POST.get('exam_name'))
			saving.save()
			messages.success(request, 'Post Created Sucessfully')
		return render(request, 'admin_create_appointment.html', appointments )
	else:
		return redirect('/')

  
def appointment_delete(request, id):
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string
	if "Admin" == group_name:
		single_appointment= Appointment.objects.get(id=id)
		single_appointment.delete()
		messages.success(request, 'Your profile was updated.')
		return redirect('/admin/create_appointment/')
	else:
		return redirect('/')

def admin_appointment_update(request,id):
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string
	if "admin" == group_name:
		user_name=request.user.get_username()#Getting Username

		#Getting all Post and Filter By Logged UserName
		appointment_list = Appointment.objects.all().order_by("-id").filter(user=request.user)
		q=request.GET.get("q") #search start
		if q:
			appointment_list=appointment_list.filter(date__icontains=q)
		else:
			appointment_list = appointment_list #search end

		single_appointment=ingle_appointment= Appointment.objects.get(id=id)
		print("heee")
		form = AppointmentForm(request.POST or None, instance=single_appointment)
		if form.is_valid():
			saving=form.save(commit=False)
			saving.user=request.user
			print("hello")
			print("hi",request.POST.get('exam_name'))
			saving.save()
			messages.success(request, 'Flight slot Created Sucessfully')
			return redirect('/admin/create_appointment/')
			    
		appointments= {
		    "query": appointment_list,
		    "user_name":user_name,
		    "form":form,
		}

		return render(request, 'admin_appointment_update.html', appointments )
	else:
		return redirect('/')