#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/5 19:01
# @Author  : zhl
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from shop import views
urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index'),
]