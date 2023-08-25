from django.contrib import admin
from .models import *
# Register your models here.
@admin.action(description="Mark selected stories as baned")
def make_ban(modeladmin, request, queryset):
    queryset.update(ban=True)

@admin.action(description="Mark selected stories as unbaned")
def make_unban(modeladmin, request, queryset):
    queryset.update(ban = False)

@admin.register(Profile)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user","created_at","ban","img",)
    list_editable = ("ban",)
    actions = [make_ban,make_unban]
    search_fields = ("user",)
    list_filter =("ban",)
