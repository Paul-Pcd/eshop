# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordermain',
            options={'verbose_name_plural': '订单中心', 'verbose_name': '订单中心', 'ordering': ('-id',)},
        ),
        migrations.RenameField(
            model_name='ordermain',
            old_name='orderid',
            new_name='order_id',
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='count',
            field=models.IntegerField(verbose_name='购买商品的数量'),
        ),
        migrations.AlterField(
            model_name='ordermain',
            name='is_pay',
            field=models.CharField(verbose_name='订单状态', choices=[('0', '未支付'), ('1', '已支付'), ('2', '已发货'), ('3', '待发货')], default='0', max_length=5),
        ),
    ]
