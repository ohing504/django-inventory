# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20171111_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Quantity'),
        ),
    ]