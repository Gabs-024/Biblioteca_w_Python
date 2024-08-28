from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.core.validators import RegexValidator, EmailValidator

from utils.geradorMatricula import gerar_matricula

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=12, default=gerar_matricula, unique=True)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=50, validators=[EmailValidator(message='Email inválido')])
    telefone = models.CharField(
        max_length=11, 
        validators=[RegexValidator(regex=r'^\d{10,11}$', message='Telefone deve ter entre 10 e 11 dígitos.')]
    )
    def __str__(self):
        return f'{self.matricula} - {self.nome}'

    def clean(self):
        error_messages = {}

        if Usuario.objects.filter(matricula=self.matricula).exclude(pk=self.pk).exists():
            error_messages['matricula'] = 'Matrícula já cadastrada.'

        if len(self.matricula) != 12:
            error_messages['matricula'] = 'Matrícula inválida. Deve conter 11 caracteres.'

        if error_messages:
            raise ValidationError(error_messages)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'