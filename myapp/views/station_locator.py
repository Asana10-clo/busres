from django.shortcuts import render

def station_locator(request):
    return render(request, 'stationloc.html')
