import re
from rest_framework import serializers


def validate_phone_number(value):
    """
    Validate that the phone number meets the following criteria:
    - Must have 11, 12, or 13 digits
    - Must be a number
    - Must start with 628
    """
    # Strip any non-numeric characters from the phone number
    value = re.sub(r'\D', '', value)

    # Check if the phone number has any non-numeric characters
    if not re.match(r'^\d+$', value):
        raise serializers.ValidationError(
            'Phone number must not have any non-numeric characters')

    # Check that the phone number is a number
    if not value.isdigit():
        raise serializers.ValidationError('Phone number must be a number')

    # Check the length of the phone number
    if len(value) not in [11, 12, 13]:
        raise serializers.ValidationError(
            'Phone number must have 11, 12, or 13 digits')

    # Check that the phone number starts with 628
    if not value.startswith('628'):
        raise serializers.ValidationError('Phone number must start with 628')
