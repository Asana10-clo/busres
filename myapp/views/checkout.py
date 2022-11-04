import json
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from ..models import Trip, Schedule, Booking


@login_required
def checkout(request, id):
    schedule = get_object_or_404(Schedule, id=id)

    context = {
        'schedule': schedule
    }

    return render(request, 'checkout.html', context)


@csrf_exempt
@require_POST
def webhook(request):
    try:
        data = json.loads(request.body)

        schedule = get_object_or_404(Schedule, id=data['schedule'])

        new_booking = Booking(
            trip=schedule.trip,
            travel_time=schedule.datetime,
            fare=schedule.trip.fare,
            reference=data['reference'],
            user=request.user
        )
        new_booking.save()

        # TODOs
        # Increment seats_booked field on the Trip model assoc. with this schedule

        if new_booking:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=500)
    except Exception:
        return HttpResponse(status=500)