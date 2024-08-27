from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from emprestimo.mixins import TodosEmprestimosMixin
from emprestimo.models import Emprestimo
from livro.mixins import HistoricoLivroMixin
from .models import Livro


# confirmar se a verificação de autenticado ou nao 
# para acessar tal pagina esta de acordo.

class ListaLivros(ListView):
    model = Livro
    template_name = 'livro/home.html'
    context_object_name = 'livros'
    paginated_by = '9'
    
class DetalhesLivro(TodosEmprestimosMixin, HistoricoLivroMixin, DetailView):
    model = Livro
    template_name = 'livro/detalhes.html'
    context_object_name = 'livro'

    def get_object(self):
        return get_object_or_404(Livro, id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        historico = self.get_historico_emprestimos()
        context[''] = historico
        return context
