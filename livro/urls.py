from django.urls import path
from .views import ListaLivros, DetalhesLivro

app_name = 'livro'

urlpatterns = [
    path('lista/', ListaLivros.as_view(), name="home"),
    path('detalhes/<int:pk>/', DetalhesLivro.as_view(), name = 'detalhes')
]
