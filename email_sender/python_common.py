# encoding:utf-8
import requests
import urllib

url = "http://api.sendcloud.net/apiv2/mail/send"

API_USER = '...'
API_KEY = '...'

mail_content = u'''<html>
<center><div style="width:800px;height:20px;background:black;text-align:center;line-height:20px;font-size:12px;"><a href="http://game.163.com/mail/2019/0408/3/" target="_blank" style="color:white;">If you cannot view this email, please click here</a></div><div style="margin:0 auto;width:800px;height:1170px;background:url(https://nie.res.netease.com/nie/mail/8HmbFJYHDB.jpg) no-repeat;overflow:hidden;"><table cellspacing="0" border="0" cellpadding="0" style="width:800px;border-collapse:collapse;"><tr style="height:2px"><td></td></tr><tr style="height:1158px"><td style="height:1158px;vertical-align:top;"><a href="https://www.cdgame.com/" title="" target="_blank" style="display:block;width:781px;height:1158px;border:0;vertical-align:top;text-align:left;overflow:hidden;float:left;margin-left:9px"><img alt="Battle with Bumblebee in C.D. Now!" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAALSURBVBhXY2AAAgAABQABqtXIUQAAAABJRU5ErkJggg==" style="width:100%;height:100%;border:0;" /></a></td></tr></table></div>
<img alt="" src="https://www.google-analytics.com/collect?v=1&tid=UA-137972691-1&cid={{}}&t=event&ec=email&ea=open"/>
</center></html>
'''
mail_content = mail_content.replace('{{}}', "4197dec442744c9f5d90800b75315cc7")

params = {
    "apiUser": "cdgame",  # 使用api_user和api_key进行验证
    "apiKey": "GIRKW2qKvvcebSei",
    "to": "wxy@tcccads.com",  # 收件人地址, 用正确邮件地址替代, 多个地址用';'分隔
    "from": "cdcommunity@tcccads.net",  # 发信人, 用正确邮件地址替代
    "fromName": "cdcommunity",
    "subject": "Battle with Bumblebee in C.D. Now!",
    "html": mail_content.encode('utf-8')
}

# filename1 = "1.txt"
# display_filename_1 = "aaa"
#
# files = {
#     "attachments": (urllib.quote(display_filename_1), open(filename1, 'rb'), 'application/octet-stream')
# }

r = requests.post(url, files=None, data=params)

print r.json()['statusCode']
