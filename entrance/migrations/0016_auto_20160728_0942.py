# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrance', '0015_auto_20160728_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aptitude_question',
            name='option_a',
            field=models.CharField(default='a.', max_length=50),
        ),
        migrations.AlterField(
            model_name='aptitude_question',
            name='option_b',
            field=models.CharField(default='b.', max_length=50),
        ),
        migrations.AlterField(
            model_name='aptitude_question',
            name='option_c',
            field=models.CharField(default='c.', max_length=50),
        ),
        migrations.AlterField(
            model_name='aptitude_question',
            name='option_d',
            field=models.CharField(default='d.', max_length=50),
        ),
        migrations.AlterField(
            model_name='chemistry_question',
            name='option_a',
            field=models.CharField(default='a.', max_length=50),
        ),
        migrations.AlterField(
            model_name='chemistry_question',
            name='option_b',
            field=models.CharField(default='b.', max_length=50),
        ),
        migrations.AlterField(
            model_name='chemistry_question',
            name='option_c',
            field=models.CharField(default='c.', max_length=50),
        ),
        migrations.AlterField(
            model_name='chemistry_question',
            name='option_d',
            field=models.CharField(default='d.', max_length=50),
        ),
        migrations.AlterField(
            model_name='english_question',
            name='option_a',
            field=models.CharField(default='a.', max_length=50),
        ),
        migrations.AlterField(
            model_name='english_question',
            name='option_b',
            field=models.CharField(default='b.', max_length=50),
        ),
        migrations.AlterField(
            model_name='english_question',
            name='option_c',
            field=models.CharField(default='c.', max_length=50),
        ),
        migrations.AlterField(
            model_name='english_question',
            name='option_d',
            field=models.CharField(default='d.', max_length=50),
        ),
        migrations.AlterField(
            model_name='math_question',
            name='option_a',
            field=models.CharField(default='a.', max_length=50),
        ),
        migrations.AlterField(
            model_name='math_question',
            name='option_b',
            field=models.CharField(default='b.', max_length=50),
        ),
        migrations.AlterField(
            model_name='math_question',
            name='option_c',
            field=models.CharField(default='c.', max_length=50),
        ),
        migrations.AlterField(
            model_name='math_question',
            name='option_d',
            field=models.CharField(default='d.', max_length=50),
        ),
        migrations.AlterField(
            model_name='physics_question',
            name='option_a',
            field=models.CharField(default='a.', max_length=50),
        ),
        migrations.AlterField(
            model_name='physics_question',
            name='option_b',
            field=models.CharField(default='b.', max_length=50),
        ),
        migrations.AlterField(
            model_name='physics_question',
            name='option_c',
            field=models.CharField(default='c.', max_length=50),
        ),
        migrations.AlterField(
            model_name='physics_question',
            name='option_d',
            field=models.CharField(default='d.', max_length=50),
        ),
    ]