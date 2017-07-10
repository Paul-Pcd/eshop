#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/5 19:01
# @Author  : zhl
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from shop import views
from .search_view import MySearchView
urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^detail/(?P<nid>\d*)/$', views.DetailView.as_view(), name='detail'),
    url(r'^list/(?P<nid>\d*)/$', views.ListView.as_view(), name='list'),
    url(r'^list_check/(?P<nid>\d*)-(?P<current_page>\d*)-(?P<ordering>\d*)/$', views.ListCheckView.as_view(), name='list_check'),

]