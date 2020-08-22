# import django system

from django.shortcuts import render, get_object_or_404

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

def location_bookstore(request, city_name):
    bookstore_model = Bookstore.objects.all()
    # insert model information to use in location_bookstore.html


    """ city_address_of_bookstore_을지로_model = bookstore_model.filter(city_address_of_bookstore='을지로')
    city_address_of_bookstore_망원동_model = bookstore_model.filter(city_address_of_bookstore='망원동')
    # to list city address of bookstore """
    # 사용 안합니다

    context = {
        'bookstores' : bookstore, 
        'bookstore' : bookstore_model
    }
    # declare variable

    return render(request, 'location_bookstore.html', context)