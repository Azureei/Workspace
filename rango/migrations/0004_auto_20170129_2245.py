# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 22:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_pageadmin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pageadmin',
            name='category',
        ),
        migrations.DeleteModel(
            name='PageAdmin',
        ),
    ]