#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/4 22:35
# @Author  : zhl
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from users import views
urlpatterns = [
    url(r'user_center_info', views.UserCenterInfoView.as_view(), name='user_center_info'),
    url(r'register', views.RegisterView.as_view(), name='register'),
]
