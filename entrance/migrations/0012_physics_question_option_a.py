# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrance', '0011_auto_20160727_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='physics_question',
            name='option_a',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
