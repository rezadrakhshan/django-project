from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Movie)
class admin_movie(admin.ModelAdmin):
    list_display = ['title','time',"star"]
    exclude = ('no_likes',)

admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Wish)

@admin.register(Message)
class admin_message(admin.ModelAdmin):
    list_display = ['calculated_time',]




