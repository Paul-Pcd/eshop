#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/5 11:36
# @Author  : zhl
# @Site    : 
# @File    : forms.py
# @Software: PyCharm
from django import forms

class RegisterForm(forms.Form):
    """验证用户注册"""
    username = forms.CharField(required=True)
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
    email = forms.EmailField(required=True, error_messages={'invalid':"不是一个有效的邮箱地址"})

class LoginForm(forms.Form):
    """登陆验证"""
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class ReceiverForm(forms.Form):
    """登陆验证"""
    username = forms.CharField(required=True)
    city = forms.CharField(required=True)
    telephone = forms.CharField(required=True)
    address = forms.CharField(required=True)


class ModifyForm(forms.Form):
    """登陆验证"""
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
