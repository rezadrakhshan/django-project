from django.contrib import admin
from blog.models import Blog , Category
# Register your models here.

@admin.action(description="تغییر به منتشر شده")
def make_published(modeladmin,request,queryset):
    obj_changed = queryset.update(status="p")
    if obj_changed == 1:
        messagee = "یک مقاله"
    else:
        messagee = "%s مقاله"%obj_changed
    modeladmin.message_user(request,f"{messagee} با موفقیت تغییر کرد")

@admin.action(description="تغییر به پیش نویس شده")
def make_draft(modeladmin,request,queryset):
    obj_change = queryset.update(status="d")
    if obj_change == 1:
        messagee = "یک مقاله"
    else:
        messagee = "%s مقاله"%obj_change 
    modeladmin.message_user(request,f"{messagee} با موفقیت تغییر کرد")
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','Image',"status",'slug','jpublish','category_to_str']
    list_filter = ['status']
    actions = [make_published,make_draft]
    prepopulated_fields = {'slug':('title',)}
    def category_to_str(self,obj):
        categories = " , ".join([category.title for category in obj.category.all()])
        if not categories:
            return "-----"
        return categories
    category_to_str.short_description = "دسته بندی ها"
@admin.register(Category)   
class Categoryadmin(admin.ModelAdmin):
    list_display = ["position","title","slug","is_active"]

        