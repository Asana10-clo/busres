from datetime import date
from .models import Trip, Point

def search_trips(departure, destination, travel_time):
    trips = Trip.objects.all().filter(
        route__departure_point__name=departure,
        route__destination_point__name=destination,
        schedules__date=travel_time
    ).order_by('fare')

    return trips


def get_locations():
    points = Point.objects.all()

    locations = []
    for point in points:
        locations.append(point.name)

    return locations
