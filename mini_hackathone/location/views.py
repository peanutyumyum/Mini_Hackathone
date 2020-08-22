# import django system

from django.shortcuts import render, get_object_or_404
from django.db.models import Q

# import models

from .models import Bookstore, City, Evaluation_about_bookstore, Informations

# Create your views here.

def location(request):
    city_model = City.objects.all()
    # insert model information to use in location.html

    context = {
        'city' : city_model,
    }
    # declare variable
    
    return render(request, 'location.html', context)

def location_filtered_bookstore(request, city_name):
    filtered_bookstore_model = Bookstore.objects.filter(city_address_of_bookstore='city_name')
    # insert model information to use in location_filtered_bookstore.html


    context = {
        'bookstore' : filtered_bookstore_model
    }
    # declare variable

    return render(request, 'location_filtered_bookstore.html', context)