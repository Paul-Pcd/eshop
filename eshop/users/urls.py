#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/5 10:34
# @Author  : zhl
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from users import views
urlpatterns = [
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^check_username/$', views.check_username, name='check_username'),
    url(r'^user_center_info/$', views.UserCenterInfoView.as_view(), name='user_center_info'),
    url(r'^user_center_order/$', views.UserCenterOrderView.as_view(), name='user_center_order'),
    url(r'^user_center_site/$', views.UserCenterSiteView.as_view(), name='user_center_site'),
]
