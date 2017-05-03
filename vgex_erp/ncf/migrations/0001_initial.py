# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ncf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer', models.IntegerField()),
                ('ultimo', models.IntegerField()),
                ('secuencia', models.IntegerField(default=0)),
                ('activo', models.BooleanField(default=False)),
            ],
        ),
    ]
