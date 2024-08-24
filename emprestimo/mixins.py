from .models import Emprestimo

class EmprestimoMixin:
    def get_emprestimos(self):
        return Emprestimo.objects.all()