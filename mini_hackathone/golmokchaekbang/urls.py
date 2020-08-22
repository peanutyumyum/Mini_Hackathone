from django.urls import path
from . import views

app_name = 'golmokchaekbang'

urlpatterns=[
    path('', views.home, name='home'),
]