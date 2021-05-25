from django.db import models

# Create your models here.
class ordersModel(models.Model):
    user_id = models.ForeignKey('users.usersModel', on_delete=models.CASCADE)
    order_location = models.CharField(blank=False, max_length=1200)
    order_quantity = models.IntegerField(blank=False)
    order_description = models.CharField(blank=True, max_length=12000)
    order_services = models.IntegerField(blank=False)

