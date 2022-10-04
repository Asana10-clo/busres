from django.db import models
from .base import BaseModel


class Trip(BaseModel):
    route = models.ForeignKey('Route', related_name='trips', on_delete=models.CASCADE)
    fare = models.DecimalField(decimal_places=2, max_digits=6, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    operator = models.ForeignKey('Operator', related_name='trips', on_delete=models.CASCADE)

    @property
    def estimated_arrival_time(self):
        if (self.route.duration is None):
            return None
        return self.time + self.route.duration

    def __str__(self):
        return '{} {}'.format(self.route, self.operator)


class TripSchedule(BaseModel):
    date = models.DateField(blank=False, null=False)
    trip = models.ForeignKey('Trip', related_name='schedules', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.trip, self.date)


class TakeOff(BaseModel):
    time = models.TimeField(blank=False, null=False)
    trip = models.ForeignKey('Trip', related_name='take_offs', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.time)