from django.contrib import admin
from .models import InstagramGallery, Team

# Register your models here.


admin.site.register(InstagramGallery)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    exclude = ["slug"]

