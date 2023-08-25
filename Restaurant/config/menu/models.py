from django.db import models
import uuid
# Create your models here.

class Menu(models.Model):
    CATEGORY = (
        ('B','breakfast'),
        ('L','lunch'),
        ('D','dinner')
    )
    title = models.CharField(max_length=25)
    detail = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media")
    price = models.IntegerField()
    category = models.CharField(max_length=1,choices=CATEGORY)
    slug = models.UUIDField(primary_key=True,default=uuid.uuid4)

    def __str__(self):
        return self.title