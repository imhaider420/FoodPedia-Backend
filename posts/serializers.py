from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import postsModel
     
class postsSerializer(serializers.ModelSerializer):
    class Meta:
        model = postsModel
        fields = (
            'user_id',
            'id',
            'title',
            'description',
            'ingredients',
            'image_path',
            'availabilty',
            )