# Generated by Django 5.1 on 2024-08-20 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0002_emprestimo_data_devolucao_emprestimo_data_emprestimo_and_more'),
        ('livro', '0005_alter_livro_data_cadastro'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='livro_emprestar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='livro.livro'),
        ),
    ]
