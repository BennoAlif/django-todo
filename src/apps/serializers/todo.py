from rest_framework import serializers
from apps.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description',
                  'completed', 'owner', 'created_at', 'updated_at']
