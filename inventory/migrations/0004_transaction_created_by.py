# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 03:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0003_auto_20171111_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='created_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
