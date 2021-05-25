from django.contrib import admin
from .models import usersModel

class usersModelAdmin(admin.ModelAdmin):
    model= usersModel


admin.site.register(usersModel, usersModelAdmin)
