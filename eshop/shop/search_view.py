#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/10 18:37
# @Author  : zhl
# @Site    : 
# @File    : search_view.py
# @Software: PyCharm
from haystack.generic_views import SearchView

class MySearchView(SearchView):
    # def get_queryset(self):
    #     # print("get_queryset")
    #     # queryset = super(MySearchView, self).get_queryset()
    #     # # further filter queryset based on some set of criteria
    #     # return queryset.filter(goods_price__gt='100')

    def get_context_data(self, *args, **kwargs):
        print("get_context_data")
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        # context['haha'] = '1'
        return context