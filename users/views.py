from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from myapp.models import Booking

@login_required
def dashboard(request):
    context = {}

    bookings = Booking.objects.filter(
        user__email=request.user.email
    )

    print(bookings)

    context = {
        'bookings': bookings
    }

    return render(request, 'dashboard.html', context)


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
