from django.shortcuts import render
from ..models import Schedule, Point


def get_locations():
    locations = []
    for point in Point.objects.all():
        locations.append(point.name)
    return locations


def search(from_point, to_point, travel_time):
    results = Schedule.objects.filter(
        trip__from_point__name=from_point,
        trip__to_point__name=to_point,
        datetime__date=travel_time
    ).order_by('trip__fare')
    return results


def index(request):
    context = {}
    context['locations'] = get_locations()
    context['schedules'] = None

    if (request.GET):
        try:
            from_point = request.GET['from']
            to_point = request.GET['to']
            travel_time = request.GET['date']

            schedules = search(from_point, to_point, travel_time)

            if request.GET.get('operator', False):
                operator = request.GET['operator']
                if operator != 'all':
                    schedules = [s for s in schedules if s.trip.operator.name == operator]

            context['schedules'] = schedules
        except Exception:
            context['errors'] = 'An error occured'

    # print(context)
    return render(request, 'index.html', context)
