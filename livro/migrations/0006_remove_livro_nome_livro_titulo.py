# Generated by Django 5.1 on 2024-08-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0005_alter_livro_data_cadastro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='nome',
        ),
        migrations.AddField(
            model_name='livro',
            name='titulo',
            field=models.CharField(default='Sem título', max_length=100),
        ),
    ]
