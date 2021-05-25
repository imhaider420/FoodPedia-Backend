from django.contrib import admin
from .models import ordersModel

class ordersModelAdmin(admin.ModelAdmin):
    model = ordersModel

admin.site.register(ordersModel, ordersModelAdmin)