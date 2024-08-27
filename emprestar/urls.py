from django.urls import path
from . import views

app_name = 'meu_emprestimo'


urlpatterns = [
    path('registrar_emprestimo/', views.registrar_emprestimo, name="registrar"),
]