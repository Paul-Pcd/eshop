#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/8 16:25
# @Author  : zhl
# @Site    : 
# @File    : simpletag.py
# @Software: PyCharm
from django import template
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def paginator(goods_category, current, ordering, current_page, page):
    url = reverse('shop:list_check', args=(goods_category, current, ordering))
    # 页面上只显示5个
    page_str = ""
    if current_page <= current < current_page + 3:
        if current == current_page:
            page_str = '<a href="#" class="active" style="background-color: #1b6d85">' + str(current) + '</a>'
        else:
            page_str = '<a href = ' + url + '>' + str(current) + '</a>'
    if current > 12:
        page_str = '<a>' + "..." + '</a>'
    if current_page < 11:
        if current > page.num_pages - 2:
            page_str = '<a href = ' + url + '>' + str(current) + '</a>'
    else:
        if current >10:
            if current == current_page:
                page_str = '<a href="#" class="active" style="background-color: #1b6d85">' + str(current) + '</a>'
            else:
                page_str = '<a href = ' + url + '>' + str(current) + '</a>'

    return page_str


@register.simple_tag
def ordering(oid):
    if oid == 1:
        return 1
    elif oid == 2:
        return 2
    else:
        return 1