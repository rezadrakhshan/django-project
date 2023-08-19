from django.db import models
from django.contrib.auth.models import User
import uuid
from extensions.utils import jalali_converter
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "دسته بند ی"
        verbose_name_plural = "دسته بندی ها"

class Blog(models.Model):
    STATUS = (
        ('p','منتشر شده'),
        ('d','منتشر نشده')
    )
    title = models.CharField(max_length=50,verbose_name="عنوان")
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="نویسنده")
    text = models.TextField(verbose_name="متن")
    status = models.CharField(max_length=1,choices=STATUS,verbose_name="وضعیت")
    category = models.ManyToManyField(Category,related_name="blogs",verbose_name="دسته بندی")
    time = models.DateTimeField(auto_now_add=True,verbose_name="زمان")
    image = models.ImageField(upload_to="media",verbose_name="تصویر")
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4,verbose_name="شاخصه")

    

    class Meta:
        verbose_name = ("مقاله")
        verbose_name_plural = ("مقالات")
        ordering = ["-time"]

    def __str__(self):
        return self.title
    
    def jpublish(self):
        return jalali_converter(self.time)
    jpublish.short_description = "زمان انتشار"


