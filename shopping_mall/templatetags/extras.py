from django import template

register = template.Library()


@register.filter(name='ranges')
def html_range(value):
    return range(value)
