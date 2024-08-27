from django.urls import include, path
from . import views

app_name = 'emprestimo'

urlpatterns = [
    path('', views.MeusEmprestimos.as_view(), name='meus_emprestimos'),
    path('emprestar/', include('emprestar.urls', namespace='emprestar')),
    path('devolver/', include('devolver.urls', namespace='devolver')),
]