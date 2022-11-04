from django.db import models
from django.core.exceptions import ValidationError
from geolocation_fields.models import fields as geo
from .base import AbstractBaseModel


class Schedule(AbstractBaseModel):
    trip = models.ForeignKey('Trip', related_name='schedules', on_delete=models.CASCADE)
    datetime = models.DateTimeField(blank=False, null=False)
    seats_total = models.PositiveIntegerField(blank=True, null=True)
    seats_booked = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return 'Schedule - {}'.format(self.datetime)


class Trip(AbstractBaseModel):
    from_point = models.ForeignKey('Point', related_name='from_point', on_delete=models.RESTRICT)
    to_point = models.ForeignKey('Point', related_name='to_point', on_delete=models.RESTRICT)
    fare = models.DecimalField(decimal_places=2, max_digits=6, null=False, blank=False)
    operator = models.ForeignKey('Operator', related_name='trips', on_delete=models.CASCADE)

    # class Meta:
    #     unique_together = (('from_point', 'to_point', 'operator'))

    def clean(self):
        # Ensure from_point and to_point are distinct
        if (self.from_point is self.to_point):
            raise ValidationError("From point and To point must be distinct")

        super(Trip, self).clean()

    def __str__(self):
        return '{} - {} {}'.format(
            self.from_point,
            self.to_point,
            self.operator
        )


class Point(AbstractBaseModel):
    name = models.CharField(max_length=60, blank=False, null=False, unique=True)
    point = geo.PointField(verbose_name='point', unique=True)
    city = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.name