from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import path
from django.contrib.auth import logout
from django.contrib import messages



def group_check(request):
	puser = request.user
	group_name=Group.objects.all().filter(user = puser)# get logget user grouped name
	try:
		group_name=str(group_name[0]) # convert to string
	except:
		my_group = Group.objects.get(name='User') 
		my_group.user_set.add(puser)
		return redirect('/user/')
	
	if "User" == group_name:
		messages.success(request,'You have successfully logged in as user')
		return redirect('/user/')
	elif "Admin" == group_name:
		messages.success(request,'You have successfully logged in as admin')
		return redirect('/admin/')

def logout_view(request):
	logout(request)
	return redirect('/')


# class register_Admin(TemplateView):
#   template_name = "register_Admin.html"

# class register_User(TemplateView):
#   template_name = "register_User.html"

