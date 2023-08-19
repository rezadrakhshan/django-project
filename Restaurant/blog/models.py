from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.html import format_html






class Post (models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    img = models.ImageField(null=True,upload_to="news_photos")


    class Meta:
        ordering = ('-publish',)

    def __str__(self) :
        return self.title
    
    def image(self):
        return format_html("<img width=95 height=60 style ='border-radius:5px;' src='{}'>".format(self.img.url))
    

class Food(models.Model):
    STATUS = (
        ('Available','available'),
        ('unavailable','Unvaibale')
    )
    food_name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100,choices=STATUS,default='Available')
    img = models.ImageField(null=True,upload_to="news_photos")

    def __str__(self) :
        return self.food_name
    
class Breakfast(models.Model):
    STATUS = (
        ('Available','available'),
        ('unavailable','Unvaibale')
    )
    food_name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100,choices=STATUS,default='Available')
    img = models.ImageField(null=True,upload_to="news_photos")

    def __str__(self) :
        return self.food_name


class Lunch(models.Model):
    STATUS = (
        ('Available','available'),
        ('unavailable','Unvaibale')
    )
    food_name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100,choices=STATUS,default='Available')
    img = models.ImageField(null=True,upload_to="news_photos")

    def __str__(self):
        return self.food_name

class Dinner(models.Model):
    STATUS = (
        ('Available','available'),
        ('unavailable','Unvaibale')
    )
    food_name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100,choices=STATUS,default='Available')
    img = models.ImageField(null=True,upload_to="news_photos")

    def __str__(self) :
        return self.food_name
    


    

    
