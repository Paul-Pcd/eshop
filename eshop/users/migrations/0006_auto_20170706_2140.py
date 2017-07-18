# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170706_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='ni_name',
            new_name='receiver_name',
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(max_length=5, choices=[('0', '注册'), ('1', '找回密码')], verbose_name='操作类型'),
        ),
    ]
