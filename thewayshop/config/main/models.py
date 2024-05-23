from django.db import models
import uuid

# Create your models here.


class InstagramGallery(models.Model):
    image = models.ImageField(upload_to="media/instagram_gallery/")
    link = models.URLField(max_length=200)
    slug = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self) -> str:
        return self.link


class Team(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to="team/")
    facebook = models.URLField(max_length=200, null=True, blank=True)
    x = models.URLField(max_length=200, null=True, blank=True)
    gmail = models.URLField(max_length=200, null=True, blank=True)
    youtube = models.URLField(max_length=200, null=True, blank=True)
    slug = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self) -> str:
        return self.name
