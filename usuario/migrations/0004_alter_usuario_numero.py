# Generated by Django 5.1 on 2024-08-21 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_alter_usuario_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='numero',
            field=models.CharField(max_length=11),
        ),
    ]
