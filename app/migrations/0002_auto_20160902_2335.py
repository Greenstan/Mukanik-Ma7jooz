# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(unique=True, max_length=255, verbose_name=b'email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=30, null=True, verbose_name=b'first name', blank=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=30, null=True, verbose_name=b'last name', blank=True),
        ),
    ]
