# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160902_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.IntegerField(null=True, blank=True)),
                ('time', models.IntegerField(null=True, blank=True)),
                ('price', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]
