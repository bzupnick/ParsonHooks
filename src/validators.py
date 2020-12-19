from django.core.exceptions import ValidationError
import re


def validate_urlable(value):
    if not re.match('^[a-zA-Z0-9-_]+$', value):
        raise ValidationError('webhook name must only contain numbers, letters, dashes, and underscores')