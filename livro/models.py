from typing import Iterable
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
    titulo = models.CharField(max_length=100, default="Sem título")
    edicao = models.CharField(max_length=15, default=1)
    autor = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField(max_length=500, null=True, blank=True, 
                default=("Aqui vai uma breve descrição sobre a historia do livro," 
                        "falando sobre quem é o personagem principal, qual a sua"
                        "historia, o que vamos encontrar e entao deixar no ar o" 
                        "que so podemos saber se ler-mos. este texto ajuda o"
                        "usuario a decidir se tem interesse ou nao em ler esse" 
                        "livro ou se ele contem as informacoes que precisa."))
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, null=True, blank=True)
    data_cadastro = models.DateField(default=timezone.now)
    emprestado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
                        