from .models import InstagramGallery
from shop.models import Category, Cart


def index(request):
    try:
        gallery = InstagramGallery.objects.all()
        category = Category.objects.filter(parent=None)
        order = Cart.objects.filter(user=request.user)
        total_price = []
        for item in order:
            price = item.product.calcute_price()
            total_price.append(int(price) * item.count)
        data = {"galleries": gallery, "categories": category, "orders": order,"total":sum(total_price)}
        return data
    except:
        return {"galleries": None, "categories": None, "orders": None}
