from django.contrib import admin
from .models import Code,Profile,FollowersCount,SuperAccount
# Register your models here.


admin.site.register(Code)
admin.site.register(Profile)
admin.site.register(FollowersCount)
admin.site.register(SuperAccount)