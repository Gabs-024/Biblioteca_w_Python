# Generated by Django 5.1 on 2024-08-27 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devolver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_devolvido', models.DateTimeField(blank=True, null=True)),
                ('entrega_atrasada', models.BooleanField(default=False)),
                ('taxa', models.CharField(default='R$0,00', max_length=8)),
            ],
        ),
    ]
