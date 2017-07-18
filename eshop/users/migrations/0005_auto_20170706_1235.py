# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170706_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiver',
            name='telephone',
            field=models.CharField(max_length=11, null=True, verbose_name='电话号码'),
        ),
    ]
