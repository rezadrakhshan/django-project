from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.html import format_html

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media",default="user.jpeg")
    address = models.CharField(max_length=200,blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4)
    ban = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    def img(self):
        return format_html("<img width=95 height=60 style ='border-radius:50px;' src='{}'>".format(self.image.url))