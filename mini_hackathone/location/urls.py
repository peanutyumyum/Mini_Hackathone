from django.urls import path
from . import views

app_name = 'location'

urlpatterns=[
    path('location/', views.location, name="location"),
    path('location/<str:city_name>', views.location_filtered_city_scale, name="location_filtered_city_scale"),
    path('location/<str:town_name>', views.location_filtered_bookstore, name="location_filtered_bookstore"),
    path('location/<str:bookstore_name>', views.location_bookstore_specific_information, name="location_bookstore_specific_information"),