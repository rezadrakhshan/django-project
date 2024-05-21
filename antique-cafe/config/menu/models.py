from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.


class Coffee(models.Model):
    name = models.CharField(max_length=50)
    small_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    medium_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    large_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    image = models.ImageField(upload_to="media")
    is_avaible = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
