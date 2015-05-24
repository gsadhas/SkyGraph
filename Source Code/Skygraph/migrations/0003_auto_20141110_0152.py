# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Skygraph', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='City',
            field=models.CharField(default='test', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Uname',
            field=models.CharField(default=datetime.date(2014, 11, 10), max_length=20),
            preserve_default=False,
        ),
    ]
