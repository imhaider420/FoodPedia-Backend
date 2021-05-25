from django.db import models
from django.contrib import admin

class reviewsModel(models.Model):
    user_id = models.ForeignKey('users.usersModel', on_delete=models.CASCADE)
    post_id = models.ForeignKey('posts.postsModel', on_delete=models.CASCADE)
    review = models.IntegerField(blank=False, max_length=5)
    title = models.CharField(blank=True, max_length=12000)
    description = models.CharField(blank=True, max_length=12000)




