from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
    



# Create your models here.


class Table(models.Model):
    name = models.CharField(max_length=50, help_text="Team Name")
    win = models.DecimalField(max_digits=10, decimal_places=0)
    draw = models.DecimalField(max_digits=10, decimal_places=0)
    lose = models.IntegerField()
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.name




