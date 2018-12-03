# coding:utf-8
from flask import Flask
from flask_mail import Mail
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=465,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='371673381@qq.com',
    MAIL_PASSWORD='goyubxohbtzfbidd',
)
mail = Mail(app)


@app.route('/index')
def index():
    # recipients接受列表
    msg = Message('this is a test',sender="123456@qq.com", recipients = ['sdfd@qq.com'])
    msg.body = 'Flask test mail'
    # 发送邮箱
    mail.send(msg)
    return 'index page'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7788, debug=True)
