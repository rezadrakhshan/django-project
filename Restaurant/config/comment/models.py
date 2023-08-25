from django.db import models
from member.models import *
import uuid
# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to="media",blank=True)
    checked = models.BooleanField(default=False)
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4)

    def __str__(self):
        return f"comment from:{self.user.user}"