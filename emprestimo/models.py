from datetime import date, timedelta
from django.db import models

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from usuario.models import Usuario


class Emprestimo(models.Model):
    nome_estudante = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING),
    data_emprestimo = models.DateTimeField(default=date.today),
    data_devolucao = models.DateTimeField(),
    data_devolvido = models.DateTimeField(blank=True, null=True),
    entrega_atrasada = models.BooleanField(default=False),
    taxa = models.CharField(default="R$0,00"),

    prazo = 3

    def save(self, *args, **kwargs):
        self.data_devolucao = self.data_emprestimo + timedelta(days=self.prazo)
        super(Emprestimo, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome_estudante
