# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170705_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('0', '注册'), ('1', '找回密码')], max_length=3, verbose_name='操作类型'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(null=True, blank=True, max_length=70, verbose_name='地址'),
        ),
    ]
