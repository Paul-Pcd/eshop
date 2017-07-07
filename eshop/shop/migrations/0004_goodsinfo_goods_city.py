# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20170707_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='goods_city',
            field=models.ForeignKey(verbose_name='商品产地', null=True, to='shop.GoodsArea'),
        ),
    ]
