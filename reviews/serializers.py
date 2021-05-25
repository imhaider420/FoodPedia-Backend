from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import reviewsModel

class reviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = reviewsModel
        fields = (
            'id',
            'user_id',
            'post_id',
            'title',
            'review',
            'description',
        )