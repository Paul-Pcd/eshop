#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/7 10:30
# @Author  : zhl
# @Site    : 
# @File    : decorate.py
# @Software: PyCharm
"""
全部用来书写装饰器函数和单个函数


"""
from django.shortcuts import redirect


def check_auth(func):
    """登陆装饰验证"""

    def inner(request, *args, **kwargs):
        if request.session.has_key('user_id'):
            return func(request, *args, **kwargs)
        else:
            return redirect('/user/login/')

    return inner
"""
之前自己构造的装饰器
def check_auth(func):

    def inner(request, *args, **kwargs):
        user_id = request.session.get('user_id')  # 是通过 去获取没有的话 就会返回一个none来进行判断也是可以的
        if user_id:
            return func(request, *args, **kwargs)
        else:
            return redirect('/user/login/')

    return inner

"""

