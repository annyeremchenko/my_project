# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20170415_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
