from django.template import Library

register = Library()


@register.filter
def split_constr(string):
    return ' '.join(string.split(';'))


@register.filter
def get_value(dictionary, key):
    try:
        return dictionary[key]
    except:
        return None