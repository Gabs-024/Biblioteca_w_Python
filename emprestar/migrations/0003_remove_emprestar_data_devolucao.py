# Generated by Django 5.1 on 2024-08-27 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emprestar', '0002_emprestar_emprestimo_obj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestar',
            name='data_devolucao',
        ),
    ]