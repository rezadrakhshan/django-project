from django.db import models
from member.models import Profile
import uuid

# Create your models here.
 

class Products(models.Model):
    TAGS = (("H", "فروش داغ"), ("D", "تخفیف ویژه"), ("N", "جدید")) 
    title = models.CharField(verbose_name="نام کالا", max_length=50)
    description = models.TextField(verbose_name="توضیحات")
    author = models.CharField(verbose_name="نویسنده", max_length=50)
    image = models.ImageField(verbose_name="تصویر", upload_to="media/products")
    page_count = models.IntegerField(verbose_name="تعداد صفحه")
    publication_date = models.CharField(max_length=50,verbose_name="سال انتشار")
    book_cover = models.CharField(verbose_name="نوع جلد", max_length=50)
    tag = models.CharField(verbose_name="تگ", max_length=1, choices=TAGS)
    price = models.IntegerField(verbose_name="قیمت", help_text="به تومان")
    discount = models.IntegerField(
        verbose_name="درصد تخفیف", help_text="چند درصد تخفیف خورده"
    )
    availble = models.BooleanField(verbose_name="موجود", default=True)

    def price_with_discount(self):
        end_price = self.price - ((self.price * self.discount) / 100)
        return int(end_price)

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self) -> str:
        return self.title


class Order(models.Model): 
    STATUS = (
        ("P", "در حال بررسی"),
        ("PR", "در حال اماده سازی"),
        ("S", "ارسال شده"),
        ("D", "تحویل داده شده"),
    )
    user = models.ForeignKey(Profile, verbose_name="خریدار", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Products, verbose_name="محصول", on_delete=models.CASCADE
    )
    status = models.CharField(verbose_name="وضعیت", max_length=2, choices=STATUS)
    slug = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارشات"

    def __str__(self) -> str:
        return f"{self.slug} for {self.user}"
