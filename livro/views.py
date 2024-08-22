from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from livro import models
from emprestimo.models import Emprestimo
from livro.models import Livro
from usuario.models import Usuario

# confirmar se a verificação de autenticado ou nao 
# para acessar tal pagina esta de acordo.


class ListaLivros(ListView):
    model = models.Livro
    template_name = '/home.html'
    context_object_name = 'livros'
    paginated_by = '9'
    
class DetalhesLivro(DetailView):
    model = models.Livro
    template_name = 'templates/detalhes.html'
    context_object_name = 'livros'

# Criar condição para exibir em data de devolvido se ainda estiver em uso.