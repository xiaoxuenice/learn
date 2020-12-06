#!/usr/bin/python
#description【 python3  mail.py xiaoxuenice@qq.com 主题 内容 】
#coding:utf-8
import smtplib,sys
from email.mime.text import MIMEText

def send_mail(rec_user,subject,content):
    smtp_host = 'smtp.163.com'
    smtp_user = '1763221232@163.com'
    smtp_pass = '********'

    msg = MIMEText(content,_subtype='plain')
    msg['Subject']=subject
    msg['From'] = smtp_user
    msg['To'] = rec_user

    server = smtplib.SMTP()
    server.connect(smtp_host)
	#如果使用了加密通信，需要开启下面的选项 默认 25端口，加密默认端口 465
	#server.starttls()
    server.login(smtp_user,smtp_pass)
    server.sendmail(smtp_user,rec_user,msg.as_string())
    server.close()

if __name__ == '__main__':
    rec_user = sys.argv[1].strip()
    subject = sys.argv[2].strip()
    content = sys.argv[3].strip()
    try:
        send_mail(rec_user,subject,content)
    except Exception as e:
        print('send error: {}.'.format(e))
    else:
        print('send to {} success!'.format(rec_user))

