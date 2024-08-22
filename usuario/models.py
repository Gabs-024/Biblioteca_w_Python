import re
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

class Usuario(models.Model):
    nome = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    matricula = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    email = models.CharField(max_length=50)
    numero = models.CharField(max_length=11)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.matricula

    def clean(self):
        error_messages = {}
        
        matricula_enviada = self.matricula or None
        matricula_salva = None
        perfil = Usuario.objects.filter(matricula=matricula_enviada).first()

        if perfil:
            matricula_salva = perfil.matricula

            if matricula_salva is not None and self.pk != perfil.pk:
                error_messages['matricula'] = 'Matricula já cadastrada.'
        
        if len(self.matricula) != 11:
            error_messages['matricula'] = 'Matrícula inválida.'

        if error_messages:
            raise ValidationError(error_messages)