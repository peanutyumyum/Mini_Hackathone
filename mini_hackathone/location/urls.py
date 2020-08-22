from django.urls import path
from . import views

app_name = 'location'

urlpatterns=[
    path('location/', views.location, name="location"),
    path('location/<int:bookstore_id>', views.location_bookstore, name="bookstore"),
]