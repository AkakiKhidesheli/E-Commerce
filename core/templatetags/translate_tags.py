from django import template
from django.utils.translation import gettext as _

register = template.Library()

@register.filter(name='translate')
def translate(value):
    return _(value)
