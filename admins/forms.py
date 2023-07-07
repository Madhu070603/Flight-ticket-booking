from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
	class Meta:
		model=Appointment
		fields=[
			"exam_name",
		    "date",
		    "time_start",
		    "capacity",
		]