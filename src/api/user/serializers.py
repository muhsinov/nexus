from rest_framework import serializers
from user.models import Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProfilerSeralizer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  
    
    class Meta:
        model = Profile
        fields = ["id", "user", "first_name", "last_name", "phone_number", "image"]