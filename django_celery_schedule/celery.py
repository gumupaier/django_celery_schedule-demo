# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 1:36 PM
# @Author  : Henson
# @Email   : henson_wu@foxmail.com
# @File    : celery.py
# @Software: PyCharm
from __future__ import absolute_import, unicode_literals

__author__ = 'henson'

from celery import Celery
import os
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_schedule.settings')  # 设置django环境

app = Celery("django_celery_schedule")

app.config_from_object(settings, namespace='CELERY')  # 使用CELERY_ 作为前缀，在settings中写配置

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)  # 发现任务文件每个app下的task.py

# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))