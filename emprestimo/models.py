from datetime import timedelta
from django.http import HttpResponse
from django.utils import timezone
from django.db import models

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
    data_devolvido = models.DateTimeField(default=timezone.now)
    entrega_atrasada = models.BooleanField(default=False)
    taxa = models.CharField(default="R$0,00", max_length=8)
    prazo = 3

    def save(self, *args, **kwargs):
        if self.livro_emprestar.emprestado:
            return HttpResponse("Livro indisponível")
        else:
            self.data_devolucao = self.data_emprestimo + timedelta(days=self.prazo)
            self.livro_emprestar.emprestado = True
            self.livro_emprestar.save()
            super(Emprestimo, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.livro_emprestar)

# Testar se o livro esta disponivel, caso esteja emprestado, impedir de fazer um emprestimo duplicado.