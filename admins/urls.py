from django.urls import path
from . import views

from django.contrib import admin

from .views import(
	admin,
	admin_appointment_list,
	appointment_delete,
	admin_appointment_update,
	)





urlpatterns = [
    path('', views.admin, name='admin_home'),
    path('slots/', views.admin, name='admin_appointment'),
    path('slot/<id>', views.edit_users, name='edit_users'),
    path('delete', views.delete_users, name='delete_users'),
    path('create_slot/', views.admin_appointment_list, name='admin_appointment_list'),
    path('create_appointment/delete/<int:id>/', appointment_delete,name='appointment_delete'),
    path('create_appointment/update/<int:id>/', admin_appointment_update,name='admin_appointment_update'),      
      
]

