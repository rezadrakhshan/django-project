from django.contrib import admin
from .models import Profile,Post,Like,Comment,FollowersCount
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user_id","username","img",)
    list_editable = ("username",)
    search_fields = ("username","user_id")

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(FollowersCount)



