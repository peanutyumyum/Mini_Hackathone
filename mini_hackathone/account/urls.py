from django.urls import path, include
from . import views
# from .views import signup, MyLoginView
# from django.contrib.auth.views import LogoutView

app_name = 'account'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name="logout"),
]