# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 20:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ncf', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ncf',
            options={'ordering': ('primer',)},
        ),
    ]