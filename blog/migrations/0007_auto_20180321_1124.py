# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-21 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180321_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]