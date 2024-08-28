import random
from datetime import datetime

def gerar_matricula():
    data_atual = datetime.now()
    ano_mes = data_atual.strftime("%Y%m")

    ultimos_digitos = random.randint(100000, 999999)

    matricula = ano_mes + str(ultimos_digitos)
    return matricula
