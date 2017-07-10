#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/10 17:10
# @Author  : zhl
# @Site    : 
# @File    : search_indexes.py
# @Software: PyCharm
from haystack import indexes
from .models import GoodsInfo

# 对指定的某个类的某些数据建立索引
class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return GoodsInfo

    def index_queryset(self, using=None):
        return self.get_model().objects.all()