from django.db import models
from datetime import date

from usuario.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__ (self) -> str:
        return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length=100),
    edicao = models.CharField(default=1),
    autor = models.CharField(max_length=100),
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING),
    data_cadastro = models.DateField(default=date.today),
    emprestado = models.BooleanField(default=False),

    def __str__(self):
        return self.nome
