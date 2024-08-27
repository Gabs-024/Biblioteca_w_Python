from pyexpat.errors import messages
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

import sys
import os

from emprestimo.models import Emprestimo
from usuario.models import Usuario

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .mixins import MeusEmprestimosMixin, TodosEmprestimosMixin
 
class ListarEmprestimos(TodosEmprestimosMixin, ListView):
    model = Emprestimo
    context_object_name = 'emprestados'
    template_name = 'emprestimo/meus_emprestimos.html'
    paginate_by = 6
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # emprestimos_atrasados = Emprestimo.objects.filter(data_devolucao__lt=self.model.data_devolvido)
        # context['emprestimos_atrasados'] = emprestimos_atrasados

        return context
    
class MeusEmprestimos(MeusEmprestimosMixin, ListView):
    model = Emprestimo
    template_name = 'emprestimo/meus_emprestimos.html'
    context_object_name = 'emprestimos'

    def get_queryset(self):
        estudante = Usuario.objects.get(usuario_id=self.request.user)
        return Emprestimo.objects.filter(nome_estudante=estudante)
    