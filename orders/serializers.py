from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import ordersModel

class ordersSerializer (serializers.ModelSerializer):
    class Meta:
        model = ordersModel
        fields = (
            'id',
            'user_id',
            'order_location',
            'order_quantity',
            'order_description',
            )
