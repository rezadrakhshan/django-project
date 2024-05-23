from .models import InstagramGallery


def index(request):
    gallery = InstagramGallery.objects.all()
    data = {"galleries": gallery}
    return data
