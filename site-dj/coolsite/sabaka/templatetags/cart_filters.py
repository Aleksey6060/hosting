from django import template
from ..utils import Cart

register = template.Library()

@register.filter
def cart_currency(value):
    return f"{float(value):.2f} руб."

@register.simple_tag
def cart_total(cart):
    if hasattr(cart, 'get_total_price'):
        return cart.get_total_price()
    return 0.00

@register.filter
def mul(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0