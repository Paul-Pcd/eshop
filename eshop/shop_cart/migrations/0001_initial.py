# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20170707_2104'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('count', models.IntegerField(verbose_name='购买数量')),
                ('create_date_time', models.DateTimeField(verbose_name='购买时间', auto_now=True)),
                ('goods_info', models.ForeignKey(to='shop.GoodsInfo', verbose_name='购买商品')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='购买用户')),
            ],
            options={
                'ordering': ('-create_date_time',),
                'verbose_name_plural': '购物车',
                'verbose_name': '购物车',
            },
        ),
    ]
