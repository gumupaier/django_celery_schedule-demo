# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 1:54 PM
# @Author  : Henson
# @Email   : henson_wu@foxmail.com
# @File    : tasks.py
# @Software: PyCharm
from __future__ import absolute_import
from django.core.cache import cache
import hashlib

__author__ = 'henson'
from celery import shared_task
from email_sender.utils.email_tools import MailSender, EmailConfigMap
import time
import os
import linecache
import random
import logging

@shared_task
def send_email(email):

    # 随机选择登录账号emailList中为要登录账号
    sort_email = random.randint(1, 10)
    login_account = linecache.getline("./email_sender/utils/emailList", sort_email).split()
    print("account:%s,password:%s" % (login_account[0], login_account[1]))
    mail_config = EmailConfigMap[login_account[0].split('@')[1]]

    print("server:%s,port:%s" % (mail_config[0], mail_config[1]))

    mailSender = MailSender(mail_config[0], mail_config[1])

    if mail_config[0] in ['smtp.gmail.com']:
        mailSender.smtp.ehlo()
        mailSender.smtp.starttls()
        mailSender.smtp.ehlo()
    mailSender.login(login_account[0], login_account[1])
    # mailSender.add_attachment("filename.doc")
    # content为发送内容
    content = ""
    result = mailSender.send("标题", content, email)
    if result:
        # 短信发送成功处理
        pass
    else:
        # 短信发送失败处理
        pass
    mailSender.close()

    return []


