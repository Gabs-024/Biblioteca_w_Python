# Generated by Django 5.1 on 2024-08-27 19:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0009_rename_numero_usuario_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=50, validators=[django.core.validators.EmailValidator(message='Email inválido')]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='Telefone deve ter entre 10 e 11 dígitos.', regex='^\\d{10,11}$')]),
        ),
    ]