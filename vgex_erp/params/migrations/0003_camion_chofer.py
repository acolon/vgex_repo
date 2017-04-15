# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('params', '0002_auto_20170415_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ficha', models.CharField(max_length=20)),
                ('capacidad', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]
