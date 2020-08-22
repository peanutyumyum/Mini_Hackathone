# import django system

from django.db.models import Q
from django.shortcuts import render

# import models

from location.models import Bookstore

# Create your views here.

def search(request):
    return render(request, 'search.html')

def result(request):
    bookstoreinfo = Bookstore.objects.all()
    query = request.GET.get('query','') 
    search_type = request.GET.get('type','')
    if query:
        if search_type == 'all':
            bookstoreinfo = bookstoreinfo.filter(Q(name__icontains=query)| Q(city_address_of_bookstore__icontains=query) | Q(trait__icontains=query)|Q(bookstore_information__icontains=query))
        elif search_type == 'name':
            bookstoreinfo = bookstoreinfo.filter(name__icontains=query)
        elif search_type == 'city_address_of_bookstore':
            bookstoreinfo = bookstoreinfo.filter(city_address_of_bookstore__icontains=query)
        elif search_type == 'trait':
            bookstoreinfo = bookstoreinfo.filter(trait__icontains=query)
        elif search_type == 'bookstore_information':
            bookstoreinfo = bookstoreinfo.filter(bookstore_information__icontains=query)
    return render(request, 'result.html',{'bookstoreinfo':bookstoreinfo , 'query':query})