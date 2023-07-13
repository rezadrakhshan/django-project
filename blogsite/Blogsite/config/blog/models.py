from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from extensions.utils import jalali_converter
# Create your models here.

class PublishedManager(models.Manager):
    def Published(self):
        return self.filter(status='p')
    
class Category(models.Model):
    title = models.CharField(max_length=50,verbose_name="عنوان دسته بندی")
    slug = models.SlugField(verbose_name="آدرس دسته بندی",unique=True)
    position = models.IntegerField(verbose_name="جایگاه")
    is_active = models.BooleanField(default=False,verbose_name="نمایش داده شود؟")
    class Meta:
        verbose_name = "دسته بند ی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ["-position"]
    
    def __str__(self) -> str:
        return self.title
    
class Blog(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),		 # draft
        ('p', "منتشر شده"),		 # publish
    )
    title = models.CharField(max_length=200, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
    description = models.TextField(verbose_name="محتوا")
    category = models.ManyToManyField(Category,related_name="blogs",verbose_name="دسته بندی")
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر مقاله")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    def __str__(self) -> str:
        return self.title
    
    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "تاریخ مقاله"
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ["-publish"]
    def Image(self):
        return format_html("<img width=90 style='border-radius:5px;' src='{}'>".format(self.thumbnail.url))
    Image.short_description = "عکس"
    objects = PublishedManager()