from django.contrib import admin
from .models import Trait, City, Bookstore, Bookstore_event, Informations

# Register your models here.
admin.site.register(Trait),
admin.site.register(City),
admin.site.register(Bookstore),
admin.site.register(Bookstore_event),
admin.site.register(Informations),