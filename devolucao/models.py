from django.utils import timezone
from django.db import models

import sys
import os

from livro.models import Livro

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from emprestimo.models import Emprestimo

class Devolucao(models.Model):
    livro_devolver = models.ForeignKey(Livro, on_delete=models.DO_NOTHING, null=True, blank=True)
    data_devolvido = models.DateTimeField(default=timezone.now)
    entrega_atrasada = models.BooleanField(default=False)
    taxa = models.CharField(default="R$0,00", max_length=8)

    def save(self, *args, **kwargs):

        if not self.livro_devolver.pk:
            raise ValueError("O objeto emprestimo não esta salvo.")
        
        livro_emprestado = Emprestimo.objects.get(livro_emprestar=self.livro_devolver)
        duracao = (self.data_devolvido.date() - livro_emprestado.data_emprestimo.date()).days
        prazo = (livro_emprestado.data_devolucao.date() - livro_emprestado.data_emprestimo.date()).days

        if duracao > prazo:
            atraso = self.duracao - prazo
            self.taxa = f'R${atraso*2},00'
        else:
            self.taxa = "R$0,00"
        
        super().save(*args, **kwargs)

        self.livro_devolver.emprestado = False
        self.livro_devolver.save()

        livro_emprestado.delete()

    def __str__(self):
        return f'{self.livro_devolver} devolvido com sucesso'