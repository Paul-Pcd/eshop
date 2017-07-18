# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_goodsinfo_goods_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='goods_images',
            field=models.ImageField(upload_to='goods/%Y/%m/%d', verbose_name='商品图片地址'),
        ),
    ]
