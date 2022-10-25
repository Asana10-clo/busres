from django.shortcuts import render
from ..utils import search_trips, get_locations


def home(request):
    if request.method == 'POST':
        departure = request.POST.get('departure')
        destination = request.POST.get('destination')
        travel_time = request.POST.get('travel_time')

        trips = search_trips(departure, destination, travel_time)

        # print([trip.fare for trip in trips]) 

        return render(request, 'display.html', {"trips": trips})
    else:
        locations = get_locations()
        return render(request, 'home.html', locals())


def mastercard(request):
    return render(request, 'mastercard.html')

