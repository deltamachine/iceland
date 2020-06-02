from django.template import Library

register = Library()

@register.filter
def split_constr(string):
    return ' '.join(string.split(';'))
