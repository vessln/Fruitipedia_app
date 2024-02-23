from django.core.exceptions import ValidationError


def validator_only_letters_in_name(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError("Fruit name should contain only letters!")

