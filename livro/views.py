from django.shortcuts import render

from emprestimo.models import Emprestimo
from livro.models import Livro
from usuario.models import Usuario

# confirmar se a verificação de autenticado ou nao 
# para acessar tal pagina esta de acordo.


def home(request):
    if request.session.get('usuario'):
        livros = Livro.objects.all(),
        usuario = Usuario.objects.get(id = request.session['usuario']),
        emprestimos = Emprestimo.objects.filter(livro = livro),
        livros_emprestar = Livros.objects.filter(usuario = usuario).filter(emprestado = False),
        return render(request, 'home.html', {'livros': livros,
                                             'emprestimos': emprestimos,
                                             'usuario_logado': request.session.get('usuario'),
                                             'id_livro': id,
                                             'livros_emprestar': livros_emprestar})
    
def detalhes(request, id):
    if request.session.get('usuario'):
        livros = Livro.objects.get(id = id)
        if request.session.get('usuario') == livros.usuario.id:
            return render(request, 'detalhe.html', {'livro': livros})
        else:
            ...

# Criar condição para exibir em data de devolvido se ainda estiver em uso.