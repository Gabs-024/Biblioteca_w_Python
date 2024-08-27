from datetime import timedelta
from django.http import HttpResponse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from emprestimo.models import Emprestimo
from livro.models import Livro
from usuario.models import Usuario

class Emprestar(models.Model):
    emprestimo_obj = models.ForeignKey(Emprestimo, on_delete=models.CASCADE, null=True, blank=True)
    nome_estudante = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, null=True, blank=True)
    livro_emprestar = models.ForeignKey(Livro, on_delete=models.DO_NOTHING, null=True, blank=True)
    data_emprestimo = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self.livro_emprestar and self.livro_emprestar.emprestado:
            raise ValueError("Livro indisponível")        
        else:
            if self.livro_emprestar:
                self.livro_emprestar.emprestado = True
                self.livro_emprestar.save()

            super(Emprestar, self).save(*args, **kwargs)
            
            if self.emprestimo_obj:
                self.emprestimo_obj.nome_estudante = self.nome_estudante
                self.emprestimo_obj.livro_emprestar = self.livro_emprestar
                self.emprestimo_obj.data_emprestimo = self.data_emprestimo
                self.emprestimo_obj.save()

    def __str__(self):
        return str(self.livro_emprestar)