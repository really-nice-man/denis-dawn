# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171216_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ready_to_register',
            field=models.BooleanField(default=False),
        ),
    ]
