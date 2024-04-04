from django import template

from teto.models import Category

register = template.Library()

@register.inclusion_tag('teto/list_categories.html')
def show_category():
    cats = Category.objects.all()
    return {"cats":cats}