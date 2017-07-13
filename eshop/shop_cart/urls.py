#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/11 11:39
# @Author  : zhl
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url

from shop_cart import views
urlpatterns = [
    url(r'^add_cart/(?P<nid>\d*)/$', views.AddCartView.as_view(), name='add_cart'),
    url(r'^update_cart/(?P<nid>\d*)/$', views.UpdateCartview.as_view(), name='update_cart'),
    url(r'^delete_goods/(?P<nid>\d*)/$', views.DeleteGoodsView.as_view(), name='delete_goods'),
    url(r'^order/$', views.OrderView.as_view(), name='order'),
    url(r'^my_cart/$', views.MyCartView.as_view(), name='my_cart'),
]