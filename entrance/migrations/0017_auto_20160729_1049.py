# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrance', '0016_auto_20160728_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='aptitude_question',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chemistry_question',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='english_question',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]