# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 02:49
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180319_1039'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OnlineEditorModel',
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
