from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Racer(AbstractUser):
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    race_age = models.FloatField(default=1)
    race_category = models.CharField(max_length=30)
    race_type = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    usac_number = models.CharField(max_length=50)
    brac_number = models.CharField(max_length=50)