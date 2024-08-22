from django import template

register = template.Library()

@register.filter
def calcula_duracao(value1, value2):
    if all((isinstance(value1, datetime), isinstance(value2, datetime))):
        dias = (value1 - value2).days
        if dias == 1:
            return f'{dias} dia'
        return f'{dias} dias'
    return "Indisponível"

# if i.data_devolvido - i.data_devolucao > 0:
#     taxa = True

