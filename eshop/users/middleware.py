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
from django.http import HttpRequest

class SaveUrlMiddleWare(object):
    """实现原页面跳回"""
    def process_request(self, request):
        url_path = request.path
        print("中间件中的url", url_path)
        url_list = ['/user/user_center_info/', '/user/user_center_order/',
                    '/user/user_center_site/', '/shop/index/', '/shop/detail/(\d*)/',
                    '/shop/list/(\d*)/',]
        if url_path in url_list:
            print('zaibuzai a ')
            request.session['url_path'] = request.get_full_path()
