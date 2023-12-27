from django.db import models
import uuid
# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media")
    facebook = models.URLField(max_length=200,blank=True,null=True)
    linkedin = models.URLField(max_length=200,null=True,blank=True)
    twitter = models.URLField(max_length=200,null=True,blank=True)
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4)
    
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to="media")
    


    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name