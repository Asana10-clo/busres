from django.shortcuts import render
from ..utils import search_trips, get_locations

def home(request):
    context = {}
    context['locations'] = get_locations()
    context['trips'] = None

    if (request.GET):
        try:
            departure = request.GET['from']
            destination = request.GET['to']
            travel_time = request.GET['date']

            # trips = search_trips(departure, destination, travel_time)
            # print([trip.fare for trip in trips])

            # Dummy data
            trips = [
                {
                    'route': 'Accra-Ho',
                    'fare': 10.00,
                    'operator': 'OA',
                    'take_off': '2022-10-27'
                }
            ]

            context['trips'] = trips
        except:
            context['errors'] = 'An error occured'

    # print(context)
    return render(request, 'home.html', context)


def mastercard(request):
    return render(request, 'mastercard.html')
