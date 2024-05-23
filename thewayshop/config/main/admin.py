from django.contrib import admin
from .models import InstagramGallery, Team,Service

# Register your models here.


admin.site.register(InstagramGallery)
admin.site.register(Service)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    exclude = ["slug"]

