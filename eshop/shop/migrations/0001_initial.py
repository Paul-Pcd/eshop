# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('city_name', models.CharField(verbose_name='商品产地', max_length=20)),
            ],
            options={
                'verbose_name': '商品产地',
                'verbose_name_plural': '商品产地',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('category_name', models.CharField(verbose_name='商品分类', max_length=20)),
                ('is_delete', models.BooleanField(verbose_name='是否删除', default=0)),
            ],
            options={
                'verbose_name': '商品分类',
                'verbose_name_plural': '商品分类',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('goods_name', models.CharField(verbose_name='商品名称', max_length=10)),
                ('goods_images', models.ImageField(verbose_name='商品图片地址', upload_to='goods/%Y/%m/%d/')),
                ('goods_price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('goods_click', models.IntegerField(verbose_name='商品点击量')),
                ('goods_unit', models.CharField(verbose_name='商品单位', max_length=10)),
                ('is_delete', models.BooleanField(verbose_name='是否删除', default=0)),
                ('goods_desc', models.TextField(verbose_name='商品描述')),
                ('goods_stock', models.IntegerField(verbose_name='商品库存', default=100)),
                ('goods_detail', tinymce.models.HTMLField()),
                ('goods_category', models.ForeignKey(verbose_name='商品分类', to='shop.GoodsCategory')),
                ('goods_city', models.ForeignKey(verbose_name='商品产地', null=True, to='shop.GoodsArea')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
                'ordering': ('id',),
            },
        ),
    ]
