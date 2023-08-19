from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils.html import format_html
# Create your models here.

class Profile(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    user_id = models.UUIDField(default=uuid.uuid4)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to="user_images",default='image.png')
    address = models.CharField(max_length=90,blank=True)
    dtime = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.username.username
    
    def img(self):
        return format_html("<img width=95 height=60 style ='border-radius:5px;' src='{}'>".format(self.image.url))
    

class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    username = models.CharField(max_length=80)
    image = models.ImageField(upload_to="images-posts")
    caption = models.TextField()
    dtime = models.DateTimeField(auto_now_add=True)
    no_likes = models.IntegerField(default=0)
    

    def __str__(self):
        return self.caption
    
class Like(models.Model):
    post_id = models.CharField(max_length=90)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.post_id
    

class Comment(models.Model):
    user = models.CharField(max_length=85)
    slug = models.CharField(max_length=10,unique=True)
    author = models.CharField(max_length=100)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    comment = models.TextField()

    def __str__(self):
        return f'{self.author} commented for {self.user}'

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
