from django.db import models
from django.contrib.auth import get_user_model
from .base import BaseModel

from myapp.models.trip import Trip

class Booking(BaseModel):
    seatNo = models.IntegerField(max_length=3, blank=False, null=False, unique=True)
    trip = models.ForeignKey(
        'Trip', related_name='trip', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

def __str__(self):
    return self.seatNo
