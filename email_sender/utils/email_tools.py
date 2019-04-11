# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 2:20 PM
# @Author  : Henson
# @Email   : henson_wu@foxmail.com
# @File    : email_tools.py
# @Software: PyCharm
__author__ = 'henson'

import smtplib
import uuid
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import os
import requests
from sendgrid import SendGridAPIClient, To, From
from sendgrid.helpers.mail import Mail
from email.header import Header
import hashlib
from email import encoders
import logging

logger = logging.getLogger(__name__)

EmailConfigMap = {
    'gmail.com': ["smtp.gmail.com", 587],
    'outlook.com': ["smtp.office365.com", 587],
    'yahoo.co.jp': ["smtp.mail.yahoo.co.jp", 587]
}


class MailSender(object):
    _from = None
    _attachments = []

    def __init__(self, smtpSvr, port):
        if port == 465:
            print("connecting...")
            self.smtp = smtplib.SMTP_SSL(smtpSvr, port)
            print("connected!!!")
        else:
            self.smtp = smtplib.SMTP()
            print("connecting...")
            ret = self.smtp.connect(smtpSvr, port)
            print(ret)
            print("connected!!!")

    def login(self, user, pwd):
        self._from = user
        print("login ...")
        self.smtp.login(user, pwd)

    def add_attachment(self, filename):
        '''
            添加附件
        '''
        att = MIMEBase('application', 'octet-stream')
        att.set_payload(open(filename, 'rb').read())
        att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', filename))
        encoders.encode_base64(att)
        self._attachments.append(att)

    def send(self, subject, content, to_addr):
        '''
            发送邮件
        '''
        msg = MIMEMultipart('alternative')
        contents = MIMEText(content, "html", _charset='utf-8')
        msg['Subject'] = subject
        msg['From'] = self._from
        msg['To'] = to_addr
        for att in self._attachments:
            msg.attach(att)
        msg.attach(contents)
        try:
            self.smtp.sendmail(self._from, to_addr, msg.as_string())
            return True
        except Exception as e:
            print(str(e))
            return False

    def close(self):
        self.smtp.quit()
        print("logout.")

