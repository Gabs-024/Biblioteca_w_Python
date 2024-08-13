from django.shortcuts import render

from Biblioteca_w_Python.livro.models import Livro

from .models import Emprestimo

def registrar_emprestimo(request):
    if request.method == 'POST':
        nome_estudante = request.POST.get('nome_estudante')
        livro_emprestado = request.POST.get('livro_emprestado')

        emprestimo = Emprestimo(nome_estudante = nome_estudante,
                                livro_id = livro_emprestado)
        
        emprestimo.save()

        livro = Livro.objects.get(id = livro_emprestado)
        livro.emprestado = True
        livro.save()

        return 