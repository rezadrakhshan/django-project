from django.db import models

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=50,help_text="name of product")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,help_text="##.##")
    is_avable = models.BooleanField(default=False)
    image = models.ImageField(upload_to="media")

    def __str__(self):
        return self.title

