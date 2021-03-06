# import os
# os.environ["DJANGO_SETTINGS_MODULE"] = "dailyfresh.settings"
# # 放到celery服务器上时添加的代码
# import django
# django.setup()



from celery import Celery
from django.conf import settings
from django.core.mail import send_mail


# 创建celery 客户端/celery 对象
# 参数1:指定任务所在的路径，从包名开始
# 参数2:指定任务队列broker, 可以作为队列的有多种，此处以redis为例
app = Celery('celery_tasks.tasks', broker='redis://192.128.115.:6379/4')

# 定义异步任务
@app.task
def send_active_email(to_email, user_name, token):
    """发送激活邮件/封装发送邮件的任务"""

    subject = "天天生鲜用户激活"  # 标题
    body = ""   # 文本邮件体
    sender = settings.EMAIL_FROM # 发件人
    receiver = [to_email]      # 接收人
    html_body = '<h1>尊敬的用户%s，感谢您注册天天生鲜！</h1>' \
                '<br><p>请点击此链接激活您的账号<a href="http://127.0.0.1:8000/users/active/%s">' \
                'http://127.0.0.1:8000/users/active/%s</a></p>' %(user_name, token, token)
    send_mail(subject, body, sender, receiver, html_message=html_body)
