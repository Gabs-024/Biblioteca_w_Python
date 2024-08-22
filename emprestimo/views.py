from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from usuario.models import Usuario
from livro.models import Livro

from .models import Emprestimo

def registrar_emprestimo(request):
    if request.method == 'POST':
        nome_estudante = request.POST.get('matricula')
        livro_emprestado = request.POST.get('livro_id')

        livro = get_object_or_404(Livro, id = livro_emprestado)

        emprestimo = Emprestimo(nome_estudante = nome_estudante,
                                livro_emprestar = livro)
        
        emprestimo.save()
        return HttpResponse ('Emprestado')
    else:
        return HttpResponse ('Algo deu errado!')

    
def listar_emprestimos(request):
    usuario = Usuario.objects.get(id = request.session['usuario']),
    livros_emprestar = Livro.objects.filter(usuario = usuario).filter(emprestado = True),
