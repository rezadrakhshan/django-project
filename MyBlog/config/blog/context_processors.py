from .models import Category
from member.models import Profile
from shop.models import Order
from django.contrib.auth.models import User





def common_data(request): 
    data = {}
    category = Category.objects.all()
    try:    
        profile = Profile.objects.get(user=request.user)
        order = Order.objects.filter(user=profile)
        data["order"] = len(order)
        data["profile"] = profile
        data["categories"] = category
    except:
        data["categories"] = category
    return data