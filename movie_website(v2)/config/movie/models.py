from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from moviepy.editor import VideoFileClip
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self) -> str:
        return self.title


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    imdb = models.FloatField(validators=[MaxValueValidator(10), MinValueValidator(0)])
    age = models.IntegerField()
    description = models.TextField()
    starring = models.TextField()
    Genres = models.ForeignKey(
        Category, related_name="category", on_delete=models.CASCADE
    )
    tag = models.ManyToManyField(Category, related_name="tags")
    file = models.FileField(upload_to="media/movie")
    trailer = models.FileField(upload_to="media/movie/trailer")
    poster = models.ImageField(upload_to="media/poster", default="media/hero.png")
    no_likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title

    @property
    def time(self):
        video = VideoFileClip(self.file.path)
        duration = video.duration
        hours = int(duration // 3600)
        min = int((duration % 3600) // 60)
        if min == 0:
            return f"{hours} h"
        elif hours == 0:
            return f"{min} min"
        else:
            return f"{hours} h {min} min"

    @property
    def star(self):
        return round(self.imdb / 2, 0)


class Message(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def calculated_time(self):
        now = timezone.now()
        time = now - self.created_at
        final_time = time.total_seconds()
        hours = int(final_time // 3600)
        min = int((final_time % 3600) // 60)
        if min == 0:
            return f"{hours} h"
        elif hours == 0:
            return f"{min} min"
        else:
            return f"{hours} h {min} min"
    
@receiver(post_save, sender=Movie)
def create_notification(sender, instance, created, **kwargs):
    if created:
        new = Message.objects.create(movie=instance,created_at=timezone.now())
        new.save()

class Like(models.Model):
    movie_id = models.CharField(max_length=20)
    user = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.movie_id


class Wish(models.Model):
    user = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.movie}"
