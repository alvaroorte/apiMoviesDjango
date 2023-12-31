# Generated by Django 4.2.5 on 2023-10-08 19:47

from django.db import migrations, models
import django.db.models.deletion
import pelicula.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, unique=True, validators=[pelicula.validators.validar_only_text])),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('resumen', models.TextField()),
                ('calificacion', models.DecimalField(decimal_places=2, max_digits=4, validators=[pelicula.validators.validar_calificacion])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('actor_principal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelicula.actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelicula.director')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelicula.genero')),
            ],
        ),
    ]
