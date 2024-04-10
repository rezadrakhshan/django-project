from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Code(models.Model):
    code = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.code

    class Meta:
        verbose_name = "کد"
        verbose_name_plural = "کد ها"

 
class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name="کاربر", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=50, verbose_name=" نام خانوداگی")
    user_name = models.CharField(max_length=50, verbose_name="نام کاربری")
    email = models.EmailField(max_length=254, verbose_name="ایمیل")
    address = models.CharField(verbose_name="آدرس", max_length=200)
    amount = models.BigIntegerField(default=0,verbose_name="اعتبار")
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل ها"


class FollowersCount(models.Model):
    follower = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name="دنبال کننده",
        related_name="follower",
    )
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name="دنبال شونده"
    )

    def __str__(self):
        return self.user.user_name
    class Meta:
        verbose_name = "دنبال کننده "
        verbose_name_plural = "دنبال کنندگان"


class SuperAccount(models.Model):
    SUPER_ACOUNT = (("G", "طلایی"), ("D", "الماسی"), ("S", "نقره ای"))
    user = models.ForeignKey(Profile, verbose_name="کاربر", on_delete=models.CASCADE)
    super_account = models.CharField(
        verbose_name="نوع اکانت", max_length=50, choices=SUPER_ACOUNT
    )
    created_at = models.DateTimeField(
        verbose_name="ساخته شده در", auto_now_add=True
    )
    slug = models.SlugField(primary_key=True, default=uuid.uuid4)
    class Meta:
        verbose_name = "حساب"
        verbose_name_plural = "حساب ها"