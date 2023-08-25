from django.db import models
import uuid
from django.utils.html import format_html
# Create your models here.


class Chefs(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=25)
    image = models.ImageField(upload_to="media")
    facebooke = models.URLField(max_length=200,blank=True,null=True)
    X = models.URLField(max_length=200,blank=True,null=True)
    instagram = models.URLField(max_length=200,blank=True,null=True)
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4)

    def __str__(self):
        return self.name
    
    def img(self):
        return format_html("<img width=95 height=60 style ='border-radius:50px;' src='{}'>".format(self.image.url))
