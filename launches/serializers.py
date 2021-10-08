from django.contrib.auth import get_user_model
from rest_framework import serializers

from launches.models import Launch, Update 
User = get_user_model()

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ('id', 'username', 'avatar')

class UpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Update
    fields = '__all__'

class PopulatedUpdateSerializer(UpdateSerializer):
  owner = NestedUserSerializer()


class LaunchSerializer(serializers.ModelSerializer):
  updates = PopulatedUpdateSerializer(many=True, read_only=True)
  following = NestedUserSerializer(many=True, read_only=True)

  class Meta:
    model = Launch
    fields = '__all__'