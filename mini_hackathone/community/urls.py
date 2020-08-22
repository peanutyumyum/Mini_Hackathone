from django.urls import path
from . import views

app_name = 'community'

urlpatterns=[
    path('community', views.community.as_view(), name='community'),
    path('community_view<pk>', views.community_view.as_view(),name="community_view"),
    path('community_delete/<pk>', views.community_delete.as_view(),name="community_delete"),
    path('community_update/<pk>', views.community_update.as_view(),name="community_update"),
    path('community_write', views.community_write.as_view(),name='community_write'),
    path('comment_write/<int:pk>', views.comment_write,name='comment_write'),
]