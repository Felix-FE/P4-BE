from launches.serializers import LaunchSerializer, UpdateSerializer
from jwt_auth.authentication import User
from django.contrib.auth.signals import user_logged_in
from rest_framework import serializers 
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

User = get_user_model()

class SignUpSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
      password = data.pop('password')
      password_confirmation = data.pop('password_confirmation')

      if password != password_confirmation:
        raise ValidationError({'password_confirmation':'does not match'})

      data['password'] = make_password(password)

      return data

    class Meta:
      model = User
      fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
  following = LaunchSerializer(many=True)
  updates_posted = UpdateSerializer(many=True)

  class Meta:
    model = User
    fields = ('username', 'avatar', 'email', 'following', 'updates_posted')