from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True, related_name="children"
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="category/", blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class ProductImage(models.Model):
    image = models.ImageField(upload_to="products/")


class Product(models.Model):
    TAG = (
        ("N", "New"),
        ("S", "Sale"),
    )
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    offer = models.IntegerField()
    count = models.IntegerField()
    picture = models.ManyToManyField(ProductImage, related_name="pic")
    size = ArrayField(models.CharField(max_length=20), blank=True, default=list, size=8)
    description = models.TextField()
    tag = models.CharField(max_length=1, choices=TAG)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    avaible = models.BooleanField(default=True)

    def calcute_price(self):
        offer = int(self.price) * self.offer / 100
        end_price = int(self.price) - offer
        return int(end_price)

    def __str__(self) -> str:
        return self.title


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    slug = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self) -> str:
        return f"{self.product.title} for {self.user.username}"
