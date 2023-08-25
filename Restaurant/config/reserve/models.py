from django.db import models
import uuid
# Create your models here.

class Table(models.Model):
    title = models.CharField(max_length=200)
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4)

    def __str__(self):
        return self.title
    
class Reserve(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    time = models.CharField(max_length=200)
    no_of_people = models.CharField(max_length=20)
    request = models.TextField()

    def __str__(self):
        return f"{self.name} in {self.time}"