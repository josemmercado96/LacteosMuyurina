# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 00:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalleventa',
            old_name='venta',
            new_name='cliente',
        ),
    ]
