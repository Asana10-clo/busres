from django.contrib import admin
from .models import Operator, Booking, Schedule, Trip, Point

admin.site.register(Operator)
admin.site.register(Schedule)
admin.site.register(Trip)
admin.site.register(Point)
admin.site.register(Booking)
