from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import admin

from .views import(
	group_check,
	logout_view,
	)

urlpatterns = [
      path('', LoginView.as_view(template_name='index.html'), name="home"),
      path('logout/', views.logout_view, name='logout'),
      path('group/', views.group_check, name='group'),
]