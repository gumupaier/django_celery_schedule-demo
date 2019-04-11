# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 1:36 PM
# @Author  : Henson
# @Email   : henson_wu@foxmail.com
# @File    : celery.py
# @Software: PyCharm
from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app
__all__ = ['celery_app']