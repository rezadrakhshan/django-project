from django.db import models
import uuid
from django.contrib.auth.models import User
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    user_name = models.CharField(max_length=20, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    adress = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(default="media/hero.png", upload_to="media/profile")
    slug = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self) -> str:
        return f"{self.first_name}  {self.last_name}"