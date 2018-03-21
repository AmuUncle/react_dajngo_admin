# -*- coding: UTF-8 -*-
import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send(subject,msg,toaddrs,fromaddr,smtpaddr,password):
    '''
    @subject:邮件主题
    @msg:邮件内容
    @toaddrs:收信人的邮箱地址
    @fromaddr:发信人的邮箱地址
    @smtpaddr:smtp服务地址，可以在邮箱看，比如163邮箱为smtp.163.com
    @password:发信人的邮箱密码
    '''
    mail_msg = MIMEMultipart()
    mail_msg['Subject'] = subject
    mail_msg['From'] =fromaddr
    mail_msg['To'] = ','.join(toaddrs)
    mail_msg.attach(MIMEText(msg, 'html', 'utf-8'))
    try:
        s = smtplib.SMTP()
        s.connect(smtpaddr)  #连接smtp服务器
        s.login(fromaddr,password)  #登录邮箱
        s.sendmail(fromaddr, toaddrs, mail_msg.as_string()) #发送邮件
        s.quit()
    except :
       print ("Error: unable to send email")
       print (traceback.format_exc())


def sendmail(subject, msg, toaddrs=None):
    if toaddrs is None:
        toaddrs = ["amuuncle@163.com"]
    fromaddr = "hudejie888@163.com"
    smtpaddr = "smtp.163.com"
    password = "Hudejie1012"
    send(subject, msg, toaddrs, fromaddr, smtpaddr, password)


if __name__ == '__main__':
    subject = "hello world"
    msg = "hello world"
    sendmail(subject, msg)
