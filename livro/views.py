from django.shortcuts import render

from livro.models import Livro
from usuario.models import Usuario

# confirmar se a verificação de autenticado ou nao 
# para acessar tal pagina esta de acordo.


def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livro.objects.filter(usuario = usuario)
        return render(request, 'home.html', {'livros': livros})
    
def detalhes(request, id):
    if request.session.get('usuario'):
        livros = Livro.objects.get(id = id)
        if request.session.get('usuario') == livros.usuario.id:
            return render(request, 'detalhe.html', {'livro': livros})
        else:
            ...

# Criar condição para exibir em data de devolvido se ainda estiver em uso.