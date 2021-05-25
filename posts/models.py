from django.db import models

# Create your models here.
class postsModel(models.Model):
    user_id = models.ForeignKey('users.usersModel', on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=120)
    description = models.CharField(blank=True, max_length=1200)
    image_path = models.CharField(blank=True, max_length=1200)
    ingredients = models.CharField(blank=True, max_length=120)
    services = models.CharField(blank=True, max_length=120)
    availabilty = models.CharField(blank=True, max_length=120)