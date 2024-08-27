from django.http import HttpResponse
from django.utils import timezone
from django.db import models


import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from emprestimo.models import Emprestimo

class Devolver(models.Model): 
    emprestimo_obj = models.ForeignKey(Emprestimo, on_delete=models.CASCADE, null=True, blank=True)   
    data_devolucao = models.DateTimeField(default=timezone.now)
    entrega_atrasada = models.BooleanField(default=False)
    taxa = models.CharField(default="R$0,00", max_length=8)

    def save(self, *args, **kwargs):
        if self.emprestimo_obj.livro_emprestar.emprestado:
            return HttpResponse("Livro indisponível")
        else:
            self.emprestimo_obj.livro_emprestar.emprestado = False
            self.emprestimo_obj.livro_emprestar.save()

            super(Devolver, self).save(*args, **kwargs)

            if self.emprestimo_obj:
                self.emprestimo_obj.data_devolucao = self.data_devolucao
                self.emprestimo_obj.entrega_atrasada = self.entrega_atrasada
                self.emprestimo_obj.taxa = self.taxa
                self.emprestimo_obj.save()

    def __str__(self):
        return str(self.emprestimo_obj)
