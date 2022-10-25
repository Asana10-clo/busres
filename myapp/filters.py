from dataclasses import fields
import django_filters

from .models import TakeOff

from myapp.models.trip import TakeOff, Trip

class TakeoffFilter(django_filters.FilterSet):

    class Meta:
        model= TakeOff
        fields =('time',)
