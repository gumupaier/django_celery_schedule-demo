# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from sendgrid import SendGridAPIClient, To, From
from sendgrid.helpers.mail import Mail

mail_content = u'''<html>
<center><div style="width:800px;height:20px;background:black;text-align:center;line-height:20px;font-size:12px;"><a href="http://game.163.com/mail/2019/0408/3/" target="_blank" style="color:white;">If you cannot view this email, please click here</a></div><div style="margin:0 auto;width:800px;height:1170px;background:url(https://nie.res.netease.com/nie/mail/8HmbFJYHDB.jpg) no-repeat;overflow:hidden;"><table cellspacing="0" border="0" cellpadding="0" style="width:800px;border-collapse:collapse;"><tr style="height:2px"><td></td></tr><tr style="height:1158px"><td style="height:1158px;vertical-align:top;"><a href="https://www.cdgame.com/" title="" target="_blank" style="display:block;width:781px;height:1158px;border:0;vertical-align:top;text-align:left;overflow:hidden;float:left;margin-left:9px"><img alt="Battle with Bumblebee in C.D. Now!" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAALSURBVBhXY2AAAgAABQABqtXIUQAAAABJRU5ErkJggg==" style="width:100%;height:100%;border:0;" /></a></td></tr></table></div>
<img alt="" src="https://www.google-analytics.com/collect?v=1&tid=UA-137972691-1&cid={{}}&t=event&ec=email&ea=open"/>
</center><p style="display:none">thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!thankyou!!</p ></html>
'''
mail_content = mail_content.replace('{{}}', "4197dec442744c9f5d90800b75315cc7")


print mail_content
message = Mail(
    from_email=From('tom@gmail.com'),
    to_emails=To('haishengwu8@gmail.com'),
    subject='Battle with Bumblebee in C.D. Now!',
    html_content=mail_content.encode("utf-8"),
    plain_text_content=u"Thank you for your investigation.".encode("utf8")
)
# try:
sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY',"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"))
response = sg.send(message)
print(response.status_code)
print(response.body)
print(response.headers)
# except Exception as e:
#     print(e.message)