#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/7 10:53
# @Author  : zhl
# @Site    : 
# @File    : middleware.py
# @Software: PyCharm
"""
页面跳转中间件 实现用户在哪个页面点击的登陆 在登陆成功后 就跳转到用户先前要访问的页面
"""
from django.http import HttpResponseRedirect


class SaveUrlMiddleWare(object):
    """实现原页面跳回"""

    def process_request(self, request):
        url_path = request.path
        url_list = ['/user/login/', '/user/register/', '/user/send_success/',
                    '/user/forget_password/', '/user/reset/']
        if url_path not in url_list:
            request.session['url_path'] = request.get_full_path()


class SimpleMiddleware(object):
    """实现登陆拦截页面的中间件"""

    def process_request(self, request):

        if request.path != '/user/login/':
            if request.session.get('username', None):
                pass
            else:
                return HttpResponseRedirect('/user/login/')
