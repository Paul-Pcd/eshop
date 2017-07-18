# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0005_auto_20170707_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('goods_price', models.DecimalField(max_digits=5, verbose_name='商品价格', decimal_places=2)),
                ('count', models.IntegerField()),
                ('goods_info', models.ForeignKey(to='shop.GoodsInfo', verbose_name='商品')),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name_plural': '订单详情',
                'verbose_name': '订单详情',
            },
        ),
        migrations.CreateModel(
            name='OrderMain',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(unique=True, verbose_name='订单编号', max_length=20)),
                ('order_time', models.DateTimeField(auto_now_add=True, verbose_name='提交订单时间')),
                ('pay_time', models.DateTimeField(verbose_name='付款时间', auto_now=True)),
                ('total', models.DecimalField(max_digits=8, verbose_name='总价格', decimal_places=2)),
                ('is_pay', models.CharField(default='0', choices=[('0', '未支付'), ('1', '已支付'), ('2', '已发货'), ('3', '待发货')], verbose_name='是否付款', max_length=5)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='购买的用户')),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name_plural': '订单详情',
                'verbose_name': '订单详情',
            },
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(to='shop_order.OrderMain', verbose_name='订单中心'),
        ),
    ]
