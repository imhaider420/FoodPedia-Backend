from django.db import models
from django.contrib.auth.models import AbstractUser

class usersModel(AbstractUser):
    address = models.CharField(blank=False , max_length= 1200)
    pNumber = models.CharField(blank=False , max_length= 120)
    image_path = models.CharField(blank=False , max_length= 120)