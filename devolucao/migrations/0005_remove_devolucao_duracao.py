# Generated by Django 5.1 on 2024-08-21 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devolucao', '0004_alter_devolucao_duracao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devolucao',
            name='duracao',
        ),
    ]