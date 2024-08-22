from django.db import models
from django.utils import timezone

from usuario.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__ (self) -> str:
        return self.nome

class Livro(models.Model):
    img = models.ImageField(upload_to='capa_livro', null=True, blank=True)
    nome = models.CharField(max_length=100, default="Sem nome")
    edicao = models.CharField(max_length=15, default=1)
    autor = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, null=True, blank=True)
    data_cadastro = models.DateField(default=timezone.now)
    emprestado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
