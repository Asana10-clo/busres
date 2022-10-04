from django.core.validators import RegexValidator
from django.db import models
from .base import BaseModel


class Operator(BaseModel):
    # Validator
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    # Fields
    name = models.CharField(max_length=30, blank=False, null=False, unique=True)
    short_name = models.CharField(max_length=10, blank=False, null=False, unique=True)
    phone = models.CharField(max_length=17, null=True, blank=True, unique=True, validators=[phone_regex])
    address = models.CharField(max_length=90, blank=True, unique=True, null=True)
    email = models.EmailField(blank=True, unique=True, null=True)
    website = models.URLField(blank=True, unique=True, null=True)

    def __str__(self):
        return self.short_name
