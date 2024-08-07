from django.shortcuts import render

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter(usuario = usuario)
        return render(request, 'home.html', {'livros': livros})
    
def detalhes(request, id):
    livros = Livros.objects.get(id = id)
    return render(request, 'detalhe.html', {'livro': livros})