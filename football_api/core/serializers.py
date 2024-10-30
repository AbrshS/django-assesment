# core/serializers.py
from rest_framework import serializers
from .models import CustomUser 

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model that includes role data.
    """
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']