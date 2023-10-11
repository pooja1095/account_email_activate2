from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    gender_choice = [
        ("male", "Male"),
        ("female", "Female"),
        ("other" ,"Other"),
        ]
    
    contact_no = models.IntegerField(null=True)
    gender = models.CharField(max_length=20, choices=gender_choice)
    address = models.TextField()
    landmark = models.TextField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.IntegerField(null=True)
