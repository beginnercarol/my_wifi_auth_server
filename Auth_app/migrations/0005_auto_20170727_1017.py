# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth_app', '0004_auto_20170727_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gw_address',
            field=models.CharField(default='192.168.1.1', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='gw_id',
            field=models.CharField(default='123456', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='gw_port',
            field=models.CharField(default='2060', max_length=100),
        ),
    ]
