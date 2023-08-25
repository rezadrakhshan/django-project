from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Reserve)
class PostAdmin(admin.ModelAdmin):
    list_display = ("name","email","time",)

admin.site.register(Table)
