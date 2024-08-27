from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from livro.models import Livro
from usuario.models import Usuario

class Emprestimo(models.Model):
    nome_estudante = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, null=True, blank=True)
    livro_emprestar = models.ForeignKey(Livro, on_delete=models.DO_NOTHING, null=True, blank=True)
    data_emprestimo = models.DateTimeField(default=timezone.now)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    entrega_atrasada = models.BooleanField(default=False)
    taxa = models.CharField(default="R$0,00", max_length=8)

    def __str__(self) -> str:
        return f'{self.livro_emprestar} emprestado com sucesso!'    