# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 05:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('entrance', '0003_remove_student_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone_no',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]