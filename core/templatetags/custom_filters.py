from django import template

register = template.Library()

@register.filter
def get_item(dictionary, value):
    return dictionary.get(value)

@register.filter
def get_page_numbers(page_obj):
    return range(1, page_obj.paginator.num_pages + 1)

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def cart_total(cart):
    return sum(item.product.price * item.quantity for item in cart)