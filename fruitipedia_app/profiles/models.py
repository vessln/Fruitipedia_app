from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia_app.profiles.validators import validator_name_starts_with_letter


class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 25
    MIN_FIRST_NAME_LENGTH = 2

    MAX_LAST_NAME_LENGTH = 35
    MIN_LAST_NAME_LENGTH = 1

    MAX_EMAIL_LENGTH = 40

    MAX_PASS_LENGTH = 20
    MIN_PASS_LENGTH = 8

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_FIRST_NAME_LENGTH),
            validator_name_starts_with_letter,
        ],
        null=False,
        blank=False,
        verbose_name="",
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_LAST_NAME_LENGTH),
            validator_name_starts_with_letter,
        ],
        null=False,
        blank=False,
        verbose_name="",
    )

    email = models.EmailField(
        max_length=MAX_EMAIL_LENGTH,
        unique=True,
        null=False,
        blank=False,
        verbose_name="",
    )

    password = models.CharField(
        max_length=MAX_PASS_LENGTH,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(MIN_PASS_LENGTH),
        ],
        verbose_name="",
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=18,
    )




