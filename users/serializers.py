# users/serializers.py

from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'email', 'profile_picture', 'is_verified', 'id', 'password', 'is_banned', 'internal_revenew_required', 'is_limit', 'account_number', 'balance', 'city', 'country', 'date_of_birth', 'account_type', 'gender', 'home_address', 'zipcode', 'pin']
        extra_kwargs = {'password': {'write_only': True}, 'first_name': {'required': True}, 'last_name': {'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.balance = validated_data.get('balance', instance.balance)
        instance.save()
        return instance
 
 
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            # Check if a user with the provided email exists
            try:
                user = User.objects.get(email=email)
                print(f'First Log {user}')
            except User.DoesNotExist:
                msg = {'error': 'User with this email does not exist.'}
                raise serializers.ValidationError(msg, code='authorization')
            # Now, authenticate the user with the provided password
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            print(f'Second Log {user}')
            if not user:
                msg = {'error': 'Unable to log in with provided credentials.'}
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = {'error': 'Must include "email" and "password".'}
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
