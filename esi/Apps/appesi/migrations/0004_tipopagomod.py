# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appesi', '0003_cursomod_tipocursof'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipopagomod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
