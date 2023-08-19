from django.contrib import admin
from .models import Category,Item,Order,CheckoutOrder
# Register your models here.


admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(CheckoutOrder)

