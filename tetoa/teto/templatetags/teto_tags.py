from django import template


from teto.models import *

register = template.Library()

@register.inclusion_tag('teto/list_categories.html')
def show_category():
    cats = Category.objects.all()
    return {"cats":cats}

@register.inclusion_tag('teto/list_tags.html')
def show_all_tags():
    return {'tags': TetoTagPost.objects.all()}