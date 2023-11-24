from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Table

@receiver(post_save, sender=Table)
def calculated_point(sender,instance,**kwargs):
    instance.point = instance.win * 3 + instance.draw
    instance.save(update_fields=['point'])