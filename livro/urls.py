from django.urls import path
from .views import ListaLivros, DetalhesLivro

urlpatterns = [
    path('', ListaLivros.as_view(), name="home"),
    path('detalhes/<int:id>', DetalhesLivro.as_view, name = 'DetalhesLivro')
]
