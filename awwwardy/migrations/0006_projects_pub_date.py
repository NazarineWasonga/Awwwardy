# -*- coding: utf-8 -*-
# Generated by Django 3.1.7 on 2021-04-06 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwwards', '0005_auto_20181019_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
