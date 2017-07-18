# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_order', '0002_auto_20170714_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermain',
            name='pay_time',
            field=models.DateTimeField(null=True, verbose_name='付款时间', blank=True),
        ),
    ]
