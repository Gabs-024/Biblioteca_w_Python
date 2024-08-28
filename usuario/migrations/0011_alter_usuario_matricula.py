# Generated by Django 5.1 on 2024-08-27 21:17

import utils.geradorMatricula
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0010_alter_usuario_email_alter_usuario_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='matricula',
            field=models.CharField(default=utils.geradorMatricula.gerar_matricula, max_length=12, unique=True),
        ),
    ]