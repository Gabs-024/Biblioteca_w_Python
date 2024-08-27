from django.shortcuts import get_object_or_404, redirect, render

from emprestar.models import Emprestar
from emprestimo.models import Emprestimo
from livro.models import Livro
from usuario.models import Usuario

def registrar_emprestimo(request):
    livro_emprestado = request.POST.get('id')
    nome_estudante = request.POST.get('nome_estudante')

    livro = get_object_or_404(Livro, id=livro_emprestado)
    nome = get_object_or_404(Usuario, usuario_id=nome_estudante)

    emprestimo = Emprestar(nome_estudante=nome, livro_emprestar=livro)
    obj_emprestimo = Emprestimo(nome_estudante=nome, livro_emprestar=livro)

    if not livro.emprestado:
        emprestimo.save()
        obj_emprestimo.save()
    else:
        return redirect('livro:home')

    return redirect('emprestimo:meus_emprestimos')