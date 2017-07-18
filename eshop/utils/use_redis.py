#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/10 22:29
# @Author  : zhl
# @Site    : 
# @File    : use_redis.py
# @Software: PyCharm
from django.conf import settings
import json
from django_redis import get_redis_connection

CON = get_redis_connection('default')


class UseRedis():
    @classmethod
    def read_from_cache(cls, user_name, key):
        key = str(user_name) + "-" + str(key)
        value = CON.get(key)
        if value == None:
            data = None
        else:
            data = json.loads(value.decode('utf-8'))
        return data

    # write cache user id
    @classmethod
    def write_to_cache(cls, user_name, key, content):
        content = json.dumps(content)
        key = str(user_name) + "-" + str(key)
        CON.set(key, content)
