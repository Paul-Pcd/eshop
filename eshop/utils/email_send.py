#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/6 17:35
# @Author  : zhl
# @Site    : 
# @File    : email_send.py
# @Software: PyCharm
import random, string
import hashlib

from users.models import EmailVerifyRecord

from django.core.mail import send_mail
from django.conf import settings


def random_str():
    """生成8位验证码"""
    str = ''
    chars = string.ascii_letters + string.digits
    length = len(chars) - 1
    ran = random.Random()
    for i in range(8):
        str += chars[ran.randint(0, length)]
    m = hashlib.md5() # 采用md5 加密
    m.update(str)
    ret = m.hexdigest() # 进行加密 不把加完密的字符串存入到数据库
        # 进行验证的时候 取出进行验证
    return str


def send_email(email, send_type="注册"):
    email_record = EmailVerifyRecord()
    random_code = random_str()
    email_record.email = email
    email_record.code = random_code
    email_record.send_type = send_type
    email_record.save()
    email_title = ""
    email_body = ""
    if send_type == "注册":
        email_title = '欢迎注册'
        a_href = "http://127.0.0.1:8000/user/active/{0}".format(random_code)
        email_body = '<a href=' + a_href + '>欢迎注册 点击下面的连接进行激活:' + a_href + '</a>'
    elif send_type == "忘记密码":
        email_title = '密码重置'
        a_href = "http://127.0.0.1:8000/user/reset/{0}".format(random_code)
        email_body = '<a href=' + a_href + '>点击下面的连接进行密码重置:' + a_href + '</a>'
    statue = send_mail(email_title, '', settings.EMAIL_FROM, [email], html_message=email_body)
    return statue
