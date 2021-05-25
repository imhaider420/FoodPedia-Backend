from django.contrib import admin
from .models import reviewsModel
# Register your models here.

class reviewsModelAdmin(admin.ModelAdmin):
    model = reviewsModel

admin.site.register(reviewsModel, reviewsModelAdmin)