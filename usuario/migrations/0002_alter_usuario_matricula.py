# Generated by Django 5.1 on 2024-08-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='matricula',
            field=models.IntegerField(),
        ),
    ]
