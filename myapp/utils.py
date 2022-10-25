from datetime import date
from django.contrib.auth import get_user_model

from myapp.models.booking import Booking

from .models.trip import TripSchedule
from .models import Trip, Point

def search_trips(departure, destination, travel_time):
    
    trips = Trip.objects.filter(
        route__departure_point__name__contains=departure,
        route__destination_point__name__contains=destination,
        take_off__date = travel_time,
        # schedules__date=travel_time
    ).order_by('fare')

    # trips = TripSchedule.objects.filter(
    #     trip__route__departure_point__name__contains=departure,
    #     trip__route__destination_point__name__contains=destination,
    #     date=travel_time
    # ).order_by('trip__fare')

    # trips = Trip.objects.all()

    return trips


def get_locations():
    points = Point.objects.all()

    locations = []
    for point in points:
        locations.append(point.name)

    return locations


def get_booking():
    
    bookings = Booking.objects.filter(
        user__email=get_user_model().email
    )

    return bookings