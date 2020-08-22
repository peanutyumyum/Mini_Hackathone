from django.urls import path
from . import views

app_name = 'location'

urlpatterns=[
    path('location/', views.location, name="location"),
    path('location/<str:city_name>', views.location_filtered_bookstore, name="bookstore"),
]