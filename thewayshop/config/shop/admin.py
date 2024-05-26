from django.contrib import admin
from .models import Category,Product,ProductImage
# Register your models here.


admin.site.register(Category)
admin.site.register(ProductImage)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','calcute_price']