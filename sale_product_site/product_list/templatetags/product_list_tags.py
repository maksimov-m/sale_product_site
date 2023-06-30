import requests
from django import template

register = template.Library()


@register.simple_tag()
def get_categories():
    r = requests.get(f'http://45.143.94.139/Discount/Products/Types')
    categories = r.json()
    mass = []
    return categories