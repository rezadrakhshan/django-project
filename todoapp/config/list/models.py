from django.db import models
import uuid
# Create your models here.


class List(models.Model):
    STATUS_CHOICES  = (
        ('A','active'),
        ('C','completed')
    )
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4)

        

    def __str__(self):
        return self.title