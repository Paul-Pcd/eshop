# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170705_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='收货人名字', null=True, max_length=20)),
                ('city', models.CharField(verbose_name='城市', null=True, max_length=30, blank=True)),
                ('address', models.CharField(verbose_name='详细地址', null=True, max_length=70)),
                ('telephone', models.IntegerField(verbose_name='联系电话')),
            ],
            options={
                'verbose_name': '收货人',
                'verbose_name_plural': '收货人',
                'ordering': ('id',),
            },
        ),
        migrations.AlterModelOptions(
            name='emailverifyrecord',
            options={'verbose_name': '邮箱验证', 'verbose_name_plural': '邮箱验证', 'ordering': ('send_date',)},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(verbose_name='城市', null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(verbose_name='详细地址', null=True, max_length=70, blank=True),
        ),
        migrations.AddField(
            model_name='receiver',
            name='user',
            field=models.ForeignKey(verbose_name='账户拥有着', to=settings.AUTH_USER_MODEL),
        ),
    ]
