from django.urls import path
from . import views

app_name = 'community'

urlpatterns=[
    path('community', views.community, name='community'),
    path('community_detil', views.community_detail, name='community_detail'),
    path('community_write', views.community_write, name='community_write'),
]