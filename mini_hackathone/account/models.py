from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    nickname=models.CharField(max_length=100)
    age= models.PositiveIntegerField(null=True, blank=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='following')