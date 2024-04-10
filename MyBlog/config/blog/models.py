from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
import uuid
from extensions.utils import jalali_converter
from member.models import Profile

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class IpAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="آدرس آیپی")


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    category = models.ForeignKey(
        Category, verbose_name="دسته بندی", on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(Category, verbose_name="تگ ها", related_name="tags")
    author = models.ForeignKey(Profile, verbose_name="نویسنده", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="ساخته شده در")
    text = RichTextUploadingField()
    is_published = models.BooleanField(default=False, verbose_name="منشتر شده")
    slug = models.UUIDField(default=uuid.uuid4, verbose_name="شناسه")
    hits = models.ManyToManyField(
        IpAddress, blank=True, related_name="hits", verbose_name="بازدیدها"
    )
    num_hits = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.title} توسط {self.author} در {self.created_at}"

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def jpublish(self):
        return jalali_converter(self.created_at)

    jpublish.short_description = "زمان انتشار"


class BlogComment(models.Model):
    user = models.ForeignKey(Profile, verbose_name="کاربر", on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, verbose_name="مقاله", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="متن")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="ساخته شده در")
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies",
        verbose_name="پاسخ به",
    )

    def __str__(self) -> str:
        return f"{self.user.user_name} برای {self.blog.title}"

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    def jpublish(self):
        return jalali_converter(self.created_at)

    jpublish.short_description = "زمان انتشار"
