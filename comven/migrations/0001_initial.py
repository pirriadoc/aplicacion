# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=50)),
                ('plataforma', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=500)),
                ('cantidad', models.IntegerField()),
                ('cliente', models.ForeignKey(to='comven.Cliente')),
            ],
        ),
    ]
