from django.contrib import admin
from .models import Products,Order
# Register your models here.

@admin.register(Products)
class admin_products(admin.ModelAdmin):
    list_display = ['title','price_with_discount',]

admin.site.register(Order)