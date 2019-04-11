
## 项目描述
- 练手项目
- django-celery demo,进行任务分发，设置定时任务
- 邮件群发，email_sender app可用于大量邮件分发，邮件轰炸


## 规范

每个为微服务定时为一单独app
创建新的微服务定时任务
```bash
python manage.py startapp xxx(app name)
```
在django setting中自行注册app



## 非docker启动方式

- 启动django服务
```bash
python manage.py runserver 13777
```

- 启动celery worker
```bash
celery worker -A django_celery_schedule -l info
```

- 启动 celery beat
```bash
celery -A django_celery_schedule beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

## docker启动方式（推荐）
```bash
docker-compose up 
```
如有大量任务，自行修改docker-compose.yml文件，多创建几个worker
