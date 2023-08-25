from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Menu)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","price","category",)
    list_editable = ("price","category",)
    list_filter =("category",)
    search_fields = ("title",)
