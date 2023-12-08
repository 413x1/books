from django import template
from django.template.defaultfilters import floatformat

register = template.Library()

@register.filter(name='format_idr')
def format_idr(value):
    formatted_value = "{:,.2f}".format(value).replace(",", ".")
    return f"Rp. {formatted_value}"
