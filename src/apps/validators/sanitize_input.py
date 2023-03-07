from django.db.models import CharField, TextField
import bleach


def sanitize_input(input_value):
    """Sanitizes input value using Bleach"""
    allowed_tags = ['p', 'br', 'strong', 'em', 'a']
    allowed_attrs = {'*': ['class', 'href']}
    cleaned = bleach.clean(
        input_value, tags=allowed_tags, attributes=allowed_attrs)
    return cleaned
