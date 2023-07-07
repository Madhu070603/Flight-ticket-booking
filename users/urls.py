from django.urls import path
from . import views

from django.contrib import admin

from .views import(
	user,
	quick_appointmnet,
	appointment_book,
    appointment_book_check,
    signup,
	)

urlpatterns = [
    path('', views.user, name='user'),
    path('my_slots', views.user, name='user'),
    path('book_slot', views.quick_appointmnet, name='quick_appointmnet'),   
    path('signup', views.signup, name='signup'),   
    path('update/<int:id>', views.appointment_book,name='appointment_update'),
    path('check/<int:id>/', views.appointment_book_check,name='appointment_book_check'),
      
]
