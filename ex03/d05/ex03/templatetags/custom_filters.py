from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    # * Permite acceder a un elemento de un diccionario usando una variable como clave.
    # * Uso en el template: {{ mi_diccionario|get_item:mi_variable }}
    if dictionary is None:
        return None
    return dictionary.get(key)