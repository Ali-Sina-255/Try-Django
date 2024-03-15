from django.core.exceptions import ValidationError

validate_unite_meassurements = ['pounds', 'lbs', 'oz', 'gram']


def validate_unite_mesasure(value):
    if value not in validate_unite_meassurements:
        raise ValidationError(F"{value} is not a valid measure")