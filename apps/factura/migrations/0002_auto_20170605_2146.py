# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autorizacion',
            name='actividad',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='factura.Actividad'),
        ),
    ]
