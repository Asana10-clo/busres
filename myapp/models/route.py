from django.core.exceptions import ValidationError
from django.db import models
from .base import BaseModel
from geolocation_fields.models import fields as geo


class Route(BaseModel):
    departure_point = models.ForeignKey('Point', related_name='routes_departure', on_delete=models.RESTRICT)
    destination_point = models.ForeignKey('Point', related_name='routes_destination', on_delete=models.RESTRICT)
    duration = models.DurationField(null=True, blank=True)  # estimated average

    class Meta:
        unique_together = (('departure_point', 'destination_point'))

    def clean(self):
        # Ensure departurePoint and destinationPoint are distinct
        if (self.departure_point.name is self.destination_point.name):
            raise ValidationError("Departure point and destination point must be distinct.")
        super(Route, self).clean()

    def __str__(self):
        return '{}-{}'.format(self.departure_point.name, self.destination_point.name)


class Point(BaseModel):
    name = models.CharField(max_length=60, blank=False, null=False, unique=True)
    point = geo.PointField(verbose_name='point', unique=True)
    town = models.CharField(max_length=60, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.name
