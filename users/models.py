from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    id = models.BigIntegerField(null=True)
    phone_number = models.BigIntegerField(null=True)

    def __str__(self):
        return self.phone_number