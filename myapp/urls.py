from django.urls import path
from . import views

urlpatterns = [
    #homepage
    path('', views.index, name='index'),
    path('contact/', views.contact,name='contact'),
    
    
]