from django.conf import settings
from django.db import models
from django.utils import timezone

from account.models import CustomUser

# Create your models here.

class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    hit = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

    @property
    def update_counter(self):
        self.hit = self.hit +1
        self.save()

class Comment(models.Model):
    objects = models.Manager()
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    create = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.content