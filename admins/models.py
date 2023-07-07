from django.db import models
from django.conf import settings

# Database creation for teacher appintment.
from django.db import models

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, blank=True, null=True)
    date = models.CharField(max_length=50)
    time_start = models.CharField(max_length=50)
    time_end = models.CharField(max_length=50)
    room_number = models.CharField(max_length=50)
    appointment_with = models.CharField(max_length=50, blank=True)
    update_time = models.DateField(auto_now=True, auto_now_add=False)
    first_time = models.DateField(auto_now=False, auto_now_add=True)
    exam_name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(default=1)
    booked_count = models.PositiveIntegerField(default=0)

    def appointments_with(self):
        return self.appointment_with
    
    def __str__(self):
        return self.exam_name

    def is_full(self):
        return self.booked_count >= self.capacity

    def book_slot(self, user):
        if self.user == user:
            return False  # User who created the appointment cannot book it

        if not self.is_full():
            self.booked_count += 1
            self.save()
            return True

        return False

    def close_booking(self):
        self.capacity = self.booked_count
        self.save()

    def is_booked(self, user):
        print("HI")
        print(self.appointment_with)
        if self.appointment_with == '':
            return False 
        users = self.appointment_with.split(',')
        print(users)
        return str(user) in users