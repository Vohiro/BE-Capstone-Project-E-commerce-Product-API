from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model, authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'role',
            'is_active',
            'date_joined'
        ]
        read_only_fields = ["id", "role", "is_active", "date_joined"]



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return  {'user': user}
        raise serializers.ValidationError('Invalid credentials')