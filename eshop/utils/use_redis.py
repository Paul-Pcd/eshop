#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/10 22:29
# @Author  : zhl
# @Site    : 
# @File    : use_redis.py
# @Software: PyCharm
from django.conf import settings
# from django.core.cache import cache
import json
from django_redis import get_redis_connection
CON = get_redis_connection('default')

class UseRedis():
    @classmethod
    def read_from_cache(cls, user_name):
        key = 'user_id_' + str(user_name)
        value = CON.get(key)
        if value == None:
            data = None
        else:
            data = json.loads(value.decode('utf-8'))
        return data

    # write cache user id
    @classmethod
    def write_to_cache(cls, user_name, content):
        content = json.dumps(content)
        key = 'user_id_' + str(user_name)
        CON.set(key, content)


