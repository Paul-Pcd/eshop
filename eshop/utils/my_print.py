#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/8 17:24
# @Author  : zhl
# @Site    : 
# @File    : my_print.py
# @Software: PyCharm


_flag = True  # 控制打印的变量


# 执行打印的函数
def my_print( *args, sep=' ', end='\n', file=None):
    if _flag:
        print(*args, sep=' ', end='\n', file=None)
