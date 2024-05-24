from django.db import models

# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True, related_name="children"
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="category/",blank=True,null=True)

    def __str__(self) -> str:
        return self.title
