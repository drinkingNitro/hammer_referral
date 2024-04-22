from django.db import models
from phonenumbers import parse as parse_phone_number
from phonenumbers.phonenumberutil import is_valid_number


class PhoneNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 20)
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        try:
            parsed_number = parse_phone_number(value, None)
            if not is_valid_number(parsed_number):
                raise ValueError('Invalid phone number')
        except Exception as e:
            raise ValueError('Invalid phone number format') from e
