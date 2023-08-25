from django.contrib import admin
from .models import *
# Register your models here.

@admin.action(description="Mark selected stories as checked")
def make_cheked(modeladmin, request, queryset):
    queryset.update(checked=True)

@admin.action(description="Mark selected stories as unchecked")
def make_unchecked(modeladmin, request, queryset):
    queryset.update(checked = False)

@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user","email","subject","checked",)
    list_filter =("checked",)
    actions = [make_cheked,make_unchecked]
    search_fields = ("user",)
    list_editable = ("checked",)