from member.models import Profile
from .models import Message
from django.urls import resolve


def common_data(request):
    data = {}
    url_name = resolve(request.path).url_name
    if (
        url_name == "home"
        or url_name == "wishlist"
        or url_name == "popular"
        or url_name == "anime"
        or url_name == "sport"
        or url_name == "action"
        or url_name == "search"
        or url_name == "contact"
    ):
        current_user = request.user
        profile = Profile.objects.get(user=request.user)
        data["profile"] = profile
        notification = Message.objects.all()
        data["notification"] = notification

    return data
