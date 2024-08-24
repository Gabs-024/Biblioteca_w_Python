from django.utils import timezone
from pyexpat.errors import messages
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

import sys
import os

from django.views import View

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from emprestimo.mixins import EmprestimoMixin
from usuario.models import Usuario
from livro.models import Livro

from .models import Emprestimo

def registrar_emprestimo(request):
    nome_estudante = request.POST.get('nome')
    livro_emprestado = request.POST.get('id')

    livro = get_object_or_404(Livro, id=livro_emprestado)

    emprestimo = Emprestimo(nome_estudante=nome_estudante, livro_emprestar=livro)
    emprestimo.save()

    return redirect('emprestimo:emprestados')
    
class ListarEmprestimos(EmprestimoMixin, ListView):
    model = Emprestimo
    context_object_name = 'emprestados'
    template_name = 'emprestimo/emprestados.html'
    paginate_by = 6
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # emprestimos_nao_devolvidos = Emprestimo.objects.filter(data_devolvido__isnull=True)
        # context['emprestimos_nao_devolvidos'] = emprestimos_nao_devolvidos

        # emprestimos_atrasados = Emprestimo.objects.filter(data_devolucao__lt=self.model.data_devolvido)
        # context['emprestimos_atrasados'] = emprestimos_atrasados
        context['emprestados'] = self.get_emprestimos()

        return context

@login_required
def devolver(request):
    if request.method == 'POST':
        print("Requisição POST recebida.") 

        id = request.POST.get('id')
        print(f"ID do empréstimo recebido: {id}") 

        id_livro = request.POST.get('livro_emprestar_id')
        print(f"ID do livro recebido: {id_livro}")  

        devolucao = get_object_or_404(Emprestimo, id=id)
        print(f"Empréstimo encontrado: {devolucao}") 

        livro = get_object_or_404(Livro, id = id_livro)
        print(f"Livro encontrado: {livro}") 

        if not devolucao.livro_emprestar.emprestado:
            print("Livro já foi devolvido anteriormente.")  
            return redirect('emprestimo:emprestados')
        
        devolucao.data_devolvido = timezone.now().date()
        print(f"Data de devolução registrada: {devolucao.data_devolvido}")  

        prazo = (devolucao.data_devolucao.date() - devolucao.data_emprestimo.date()).days
        duracao = (devolucao.data_devolvido - devolucao.data_emprestimo.date()).days

        if duracao > prazo:
            atraso = duracao - prazo
            devolucao.taxa = f'R${atraso*2},00'
        else:
            devolucao.taxa = "R$0,00"
        
        livro.emprestado = False
        livro.save()  
        devolucao.save()

        print(f"Emprestimo ID: {id}, Livro: {devolucao.livro_emprestar.nome}")        
        return redirect('emprestimo:emprestados')
    else:
        print("Método de requisição inválido. Esperado POST.")  
        return redirect('livros:home')