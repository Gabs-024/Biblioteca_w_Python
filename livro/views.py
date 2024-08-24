from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from emprestimo.mixins import EmprestimoMixin
from emprestimo.models import Emprestimo
from emprestimo.views import ListarEmprestimos
from .models import Livro


# confirmar se a verificação de autenticado ou nao 
# para acessar tal pagina esta de acordo.

class ListaLivros(ListView):
    model = Livro
    template_name = 'livro/home.html'
    context_object_name = 'livros'
    paginated_by = '9'
    
class DetalhesLivro(EmprestimoMixin, DetailView):
    model = Livro
    template_name = 'livro/detalhes.html'
    context_object_name = 'livro'

    def get_object(self):
        return get_object_or_404(Livro, id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        emprestimos = self.get_emprestimos()
        context['emprestados'] = emprestimos
        return context
