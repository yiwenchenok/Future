# coding=utf-8

from flask import Flask
from flask_mail import Message, Mail
from celery import Celery

# flask 实例
app = Flask(__name__)  # type:Flask

app.config['CELERY_BROKER_URL'] = 'redis://127.0.0.1:6379/15'
app.config['CELERY_RESULT_BACKEND'] = 'redis://127.0.0.1:6379/15'

# 实例化celery 对象,  celery 应用名称，需要时flask 实例的app.name
celery_app = Celery(app.name, broker=app.config["CELERY_BROKER_URL"], backend=app.config["CELERY_RESULT_BACKEND"])

# 为Celery同步Flask上的配置
celery_app.conf.update(app.config)

# 使用update形式更新邮箱配置
app.config.update(
    MAIL_SERVER='smtp.qq.com',  # 服务器地址
    MAIL_PROT=25,  # 邮件服务器端口
    MAIL_USE_TLS=True,  # 使用tls 安全协议
    MAIL_USERNAME='1820312463@qq.com',  # 发送邮箱
    MAIL_PASSWORD='zapgenybpxdibccf',  # 密码
)

# 实例化一个邮件对象
mail = Mail(app)
@app.route("/send_mail")
def send_mail():
    a = 1 + 1
    recp_list = ["1820312463@qq.com"]
    body = "来自火星的番茄"
    send_mail_celery.delay("flask", recp_list, body, app.config["MAIL_USERNAME"])

    return str(a)


# 任务函数
@celery_app.task
def send_mail_celery(sub, rep, body, sender):
    # recipients 接收者的邮箱列表，body 邮件正文，
    # cc 抄送，bcc 秘密抄送
    msg = Message(subject=sub, recipients=rep, body=body, sender=sender)

    # # 设置发送者的邮箱
    # msg.sender = sender

    # 发送附件
    # content_type 附件的类型
    msg.attach("01.jpg", content_type="image/jpeg", data=open("01.jpg", "rb").read())

    with app.app_context():
        # 获取flask 实例的上下文，
        # mail 需要flask 上下文
        mail.send(msg)
if __name__ == '__main__':
    app.run(debug=True)

    """
    celery -A test_celery_mail.celery_app worker -l info --pool=solo
    """