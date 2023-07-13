from django import template
from blog.models import Category
register = template.Library()

@register.simple_tag()
def title():
    return "جهانگردی"

@register.inclusion_tag("template_tags/navbar.html")
def navbar():
    return {
        "categories":Category.objects.filter(is_active=True)
    }