# Generated by Django 5.1 on 2024-08-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0007_emprestar_devolver_delete_emprestimo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devolver',
            old_name='data_devolvido',
            new_name='data_final',
        ),
        migrations.AddField(
            model_name='emprestar',
            name='data_devolvido',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]