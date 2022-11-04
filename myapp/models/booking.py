from django.db import models
from django.contrib.auth import get_user_model
from .base import AbstractBaseModel


class Booking(AbstractBaseModel):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE, null=True)
    travel_time = models.DateTimeField(null=True, blank=False)
    fare = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=False)
    reference = models.CharField(max_length=100, null=True)
    seat_no = models.PositiveIntegerField(blank=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.reference
