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
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^check_username/$', views.check_username, name='check_username'),
    url(r'^user_center_info/$', views.UserCenterInfoView.as_view(), name='user_center_info'),
    url(r'^user_center_order/$', views.UserCenterOrderView.as_view(), name='user_center_order'),
    url(r'^user_center_site/$', views.UserCenterSiteView.as_view(), name='user_center_site'),
    # 删除用户的收获地址url
    url(r'^modify_address/$', views.ModifyAddressView.as_view(), name='modify_address'),
    # 邮箱激活验证  修改密码等操作
    url(r'^active/(?P<active_code>.*)/$', views.ActiveView.as_view(), name='active'),
    url(r'^send_success/$', views.SendSuccessView.as_view(), name='send_success'),
    url(r'^forget_password/$', views.ForgePasswordView.as_view(), name='forget_password'),
    url(r'^reset/(?P<reset_code>.*)/$', views.ResetPasswordView.as_view(), name='reset'),
    url(r'^modify_password/$', views.ModifyView.as_view(), name='modify_password'),
]
