# Generated by Django 5.0 on 2023-12-24 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_pelicula_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='descripcion',
            field=models.CharField(default='', max_length=400),
        ),
    ]