from django.contrib import admin
from .models import (
    Operator,
    Route,
    Point,
    Trip,
    TripSchedule,
    TakeOff
)

admin.site.register(Operator)
admin.site.register(Route)
admin.site.register(Point)
admin.site.register(Trip)
admin.site.register(TripSchedule)
admin.site.register(TakeOff)
