# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Skygraph', '0003_auto_20141110_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Fname', models.CharField(max_length=20)),
                ('Lname', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=20)),
                ('Uname', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
