from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import usersModel

class usersSerializer (serializers.ModelSerializer):
    class Meta:
        model = usersModel
        fields = (
            'id',
            'password',
            'last_login',
            'is_superuser',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'is_staff',
            'date_joined',
            'pNumber',
        )
