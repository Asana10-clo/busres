from django.urls import path, include
from . import views

urlpatterns = [
    # index page
    path('', views.index, name='index'),

    # checkout page
    path('checkout/<str:id>/', views.checkout, name='checkout'),
    path('webhook/', views.webhook, name='webhook'),

    # station locator page
    path('stationloc/', views.stationloc, name='stationloc'),

    # contact page
    path('contact/', views.contact, name='contact'),

    # blog
    path('blog/', views.blog, name="blog"),
    path('blog/<str:slug>/', views.blog_post, name='blog_post'),

    # path('mastercard', views.mastercard, name='mastercard'),
    # path('confirm', views.confirm, name='confirm'),
    # path('seat', views.seat, name="seat"),
    # path('dashboard', views.dashboard, name="dashboard"),
]
