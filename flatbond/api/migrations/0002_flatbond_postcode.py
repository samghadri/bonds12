# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-02-05 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatbond',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
