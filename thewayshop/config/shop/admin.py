from django.contrib import admin
from .models import Category,Product,ProductImage,WishList,Cart,Coupon
# Register your models here.


admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(WishList)
admin.site.register(Cart)
admin.site.register(Coupon)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','calcute_price']