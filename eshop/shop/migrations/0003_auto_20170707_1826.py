# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_goodsinfo_goods_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='goods_name',
            field=models.CharField(max_length=30, verbose_name='商品名称'),
        ),
    ]
