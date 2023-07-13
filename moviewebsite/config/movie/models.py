from django.db import models
from django.utils import timezone
import uuid
# Create your models here.




class Company(models.Model):
    name = models.CharField(max_length=100)
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4)

    def __str__(self) :
        return self.name
    
class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4)
    img = models.ImageField(upload_to="news_photos")

    def __str__(self) :
        return self.title

class Movie(models.Model):
    STATUS_CHOICES = (
        ('coming soon','Coming soon'),
        ('published','Published')
    )
    
    movie_name = models.CharField(max_length=100)
    imdb = models.CharField(max_length=10)
    slug = models.SlugField(max_length=100,unique=True)
    Year_of_construction = models.IntegerField(null=True)
    publish = models.DateTimeField(default=timezone.now,null=True)
    description = models.TextField()
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default="published")
    special_offers = models.BooleanField(default=False)
    img = models.ImageField(null=True,upload_to="news_photos")
    imdb_link = models.URLField(max_length=400)
    trailer = models.FileField(upload_to="trailer",null=True)
    img2 = models.ImageField(upload_to="news_photos",null=True,blank=True)
    img3 = models.ImageField(upload_to="news_photos",null=True,blank=True)
    img4 = models.ImageField(upload_to="news_photos",null=True,blank=True)
    Family_guide = models.TextField(null=True,blank=True)
    movie_file = models.FileField(upload_to="movie_file",blank=True,null=True)
    company = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)




    def __str__(self) :
        return self.movie_name
    class Meta:
        ordering = ["-publish"]

class Message(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()

    def __str__(self) :
        return self.name
