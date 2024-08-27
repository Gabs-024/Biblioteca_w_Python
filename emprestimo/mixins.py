from urllib import request
from .models import Emprestimo

class MeusEmprestimosMixin:
    def get_meus_emprestimos(self):
        return Emprestimo.objects.filter(nome_estudante=request.user.id)
    
class TodosEmprestimosMixin:
    def get_emprestimos(self):
        return Emprestimo.objects.all()
