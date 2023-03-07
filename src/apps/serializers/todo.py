from rest_framework import serializers
from apps.models import Todo
from apps.validators import validate_phone_number, sanitize_input


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    phone_number = serializers.CharField(validators=[validate_phone_number])

    def validate(self, data):
        # Sanitize the input data using bleach
        data['description'] = sanitize_input(data['description'])
        data['title'] = sanitize_input(data['title'])

        return data

    class Meta:
        model = Todo
        fields = '__all__'
