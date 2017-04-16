# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ficha', models.CharField(max_length=20)),
                ('capacidad', models.IntegerField(default=0)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'camiones',
                'ordering': ['ficha'],
            },
        ),
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'choferes',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='PrecioGalon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(unique=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'ordering': ['-fecha'],
            },
        ),
    ]
