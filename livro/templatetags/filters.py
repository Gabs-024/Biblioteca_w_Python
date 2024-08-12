from django import template

register = template.Library()

@register.filter
def calcula_duracao(value1, value2):
    return (value1 - value2).days

# calcula taxa    

# if i.data_devolvido - i.data_devolucao > 0:
#     taxa = True

