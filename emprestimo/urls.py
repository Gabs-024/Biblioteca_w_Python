from django.urls import path
from . import views

urlpatterns = [
    path('registrar_emprestimo/', views.registrar_emprestimo, name="registrar_emprestimo"),
]