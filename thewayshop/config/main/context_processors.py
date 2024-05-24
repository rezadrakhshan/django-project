from .models import InstagramGallery
from shop.models import Category


def index(request):
    gallery = InstagramGallery.objects.all()
    category = Category.objects.filter(parent=None)
    data = {"galleries": gallery, "categories": category}
    return data
