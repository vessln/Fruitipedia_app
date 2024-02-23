from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia_app.fruit.validators import validator_only_letters_in_name
from fruitipedia_app.profiles.models import Profile


class Fruit(models.Model):
    MAX_NAME_LENGTH = 30
    MIN_NAME_LENGTH = 2

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_NAME_LENGTH),
            validator_only_letters_in_name,
        ],
        unique=True,
        error_messages={"unique": "This fruit name is already in use! Try a new one."},
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="fruits",
    )



