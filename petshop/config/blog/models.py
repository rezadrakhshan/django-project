from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4)

    def __str__(self):
        return self.title


class IpAddress(models.Model):
    ipaddress = models.GenericIPAddressField()

class Blog(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(upload_to="media")
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category,related_name="blogs")
    publish = models.BooleanField(default=False)
    hits = models.ManyToManyField(IpAddress, related_name="hits", blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4)

    def __str__(self):
        return f"{self.name} commented for {self.blog.title}"
    