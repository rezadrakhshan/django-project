
from .models import Blog


def common_data(request):
    data = {}
    popular = Blog.objects.all().order_by("-hits")[:6]
    data["popular"] = popular

    return data