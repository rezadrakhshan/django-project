from django.contrib import admin
from .models import Movie,Message,Company,Category

# Register your models here.
admin.site.register(Movie)
admin.site.register(Message)
admin.site.register(Company)
admin.site.register(Category)