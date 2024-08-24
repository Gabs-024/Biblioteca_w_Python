from django.urls import path
from . import views

app_name = 'emprestimo'


urlpatterns = [
    path('registrar_emprestimo/', views.registrar_emprestimo, name="emprestimo"),
    path('meus_emprestimos/', views.ListarEmprestimos.as_view(), name="emprestados"),
    path('devolver/', views.devolver, name="devolver"),
]