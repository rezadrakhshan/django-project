from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Chefs)
class PostAdmin(admin.ModelAdmin):
    list_display = ("name","designation","img",)
    list_editable = ("designation",)
    list_filter =("designation",)
    search_fields = ("name",)
