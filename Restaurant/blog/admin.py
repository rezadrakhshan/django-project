from django.contrib import admin
from .models import Post,Food,Breakfast,Lunch,Dinner

@admin.action(description="Mark selected stories as published")
def make_published(modeladmin, request, queryset):
    queryset.update(status="published")

@admin.action(description="Mark selected stories as drafed")
def make_draft(modeladmin, request, queryset):
    queryset.update(status="draft")
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","image","slug","author","publish","status")
    list_filter =("status","publish","created","author")
    actions = [make_published,make_draft]
    search_fields = ("title","body")
    prepopulated_fields = {"slug":("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ("publish","status")
    list_editable = ("status",)

admin.site.register(Food)
admin.site.register(Breakfast)
admin.site.register(Lunch)
admin.site.register(Dinner)
