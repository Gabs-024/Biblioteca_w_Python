# Generated by Django 5.1 on 2024-08-26 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0005_alter_emprestimo_nome_estudante'),
        ('usuario', '0009_rename_numero_usuario_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolvido',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='nome_estudante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.usuario'),
        ),
    ]
