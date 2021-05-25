from django.contrib import admin
from .models import postsModel

# Register your models here.
class postsModelAdmin(admin.ModelAdmin):
    model = postsModel

admin.site.register(postsModel, postsModelAdmin)
