import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from devolucao.models import Devolucao
from emprestimo.models import Emprestimo
from livro.models import Livro
from django.db.models import Q

def devolucao(request):
    if request.method == 'POST':
        id = request.POST.get('id_livro_devolver')
        emprestimo = get_object_or_404(Emprestimo, id=id)

        devolucao = Devolucao(emprestimo=emprestimo)
        devolucao.save()

        return HttpResponse ('Devolvido com sucesso')
    else:
        return HttpResponse ('Algo deu errado')



    