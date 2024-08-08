from django.db import models
from datetime import date

from usuario.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__ (self) -> str:
        return self.nome
    
class Emprestimos(models.Model):
    nome_estudante = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING),
    data_emprestimo = models.DateTimeField(default=date.today),
    data_devolucao = models.DateTimeField(default= date.today + 3),
    data_devolvido = models.DateTimeField(default=date.today),
    entrega_atrasada = models.BooleanField(default=False),
    taxa = models.CharField(),

    def __str__(self):
        return self.nome_estudante

class Livro(models.Model):
    nome = models.CharField(max_length=100),
    edicao = models.CharField(default=1),
    autor = models.CharField(max_length=100),
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING),
    data_cadastro = models.DateField(default=date.today),
    emprestado = models.BooleanField(default=False),

    def __str__(self):
        return self.nome
