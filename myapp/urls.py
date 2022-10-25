from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('station-locator', views.station_locator, name='station_locator'),
    path('mastercard', views.mastercard, name='mastercard'),
    path('confirm', views.confirm, name='confirm'),
    path('blog', views.blog, name='blog'),
    path('blogs', views.blogs, name="blogs"),
    path('seat', views.seat, name="seat"),
    path('dashboard', views.dashboard, name="dashboard"),


    # Added lines here
    path('display', views.display, name="display"),
    
    

]
