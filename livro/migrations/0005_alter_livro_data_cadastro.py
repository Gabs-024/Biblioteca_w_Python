# Generated by Django 5.1 on 2024-08-19 21:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0004_alter_livro_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='data_cadastro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]