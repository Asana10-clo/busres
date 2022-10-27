from django.shortcuts import render
#modification
# from myapp.models import Trip
# from myapp.models.trip import TakeOff

# def Multiplesearchtrip(request):
#     if request.method:'POST':
#         takeOff=request.POST.get('time')
#         operator=request.POST.get('operator')
#         takeoffobj=Trip.objects.row('select * from Trip where take_off="' )


def display(request):
    return render(request, 'display.html')


def seat(request):
    return render(request, 'seat.html')
