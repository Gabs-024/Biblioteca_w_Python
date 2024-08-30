from datetime import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from devolver.models import Devolver
from emprestimo.models import Emprestimo
from livro.models import Livro

def devolver(request):
    if request.method == 'POST':
        print("Requisição POST recebida.") 

        id = request.POST.get('id')
        print(f"ID do empréstimo recebido: {id}") 

        id_livro = request.POST.get('livro_emprestar_id')
        print(f"ID do livro recebido: {id_livro}")  

        emprestimo_obj = get_object_or_404(Emprestimo, id=id)
        print(f"Empréstimo encontrado: {emprestimo_obj}") 

        livro = get_object_or_404(Livro, id = id_livro)
        print(f"Livro encontrado: {livro}") 
        
        devolucao = Devolver(emprestimo_obj=emprestimo_obj)

        duracao = (devolucao.data_devolucao.date() - emprestimo_obj.data_emprestimo.date()).days
        print(duracao)

        if duracao > 3:
            devolucao.entrega_atrasada = True
            taxa = (duracao - 3) * 2
            devolucao.taxa = f"R${taxa},00"

        devolucao.save()
        print(devolucao)
        
        emprestimo_obj.data_devolucao = devolucao.data_devolucao
        emprestimo_obj.entrega_atrasada = devolucao.entrega_atrasada
        emprestimo_obj.taxa = devolucao.taxa
        livro.emprestado = False
        livro.save()
        emprestimo_obj.save()

        messages.success(request, 'Livro devolvido com sucesso!')
        return redirect('emprestimo:meus_emprestimos')
    else:
        messages.error(request, 'Tente novamente')
        return redirect('livro:home')