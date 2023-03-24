from django.contrib.auth.models import User
from rest_framework import serializers
from apps.serializers import TodoSerializer


class UserSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
