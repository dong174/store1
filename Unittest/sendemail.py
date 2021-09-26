# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
#
# def setContext(filepath, filename, context, subject):# filepath : 文件路径 filename：文件名 context: 文件正文 subject：主题
#     # 添加附件
#     with open(filepath, 'rb') as f:
#         send_att = f.read()
#
#     # 设置附件
#     att = MIMEText(send_att, 'text', 'utf-8')
#     att['Content-Type'] = 'application/octet-stream'
#     att['Content-Disposition'] = r'attachment;filename=' + filename
#
#     # 设置html格式邮件正文
#     msgtext = MIMEText(context, 'html', 'utf-8')
#
#     # 采用related定义内嵌资源的邮件体
#     msg = MIMEMultipart('related')
#     msg['Subject'] = subject
#     msg.attach(att)
#     msg.attach(msgtext)
#     return msg
#
#
# def send(msg, sender, recerive, code):# 邮件内容， 发送方，接收方，授权码
#     # 发送邮件
#     smtp = smtplib.SMTP()
#     # 发送邮件的服务器地址,例如qq邮箱（是smtp.qq.com而不是mail.qq.com哦）
#     smtp.connect('smtp.163.com')
#     # 发送方登录 用户+授权码（非密码）
#     smtp.login(sender, code)
#     # 发送短信 发件方+收件方
#     smtp.sendmail(sender, recerive, msg.as_string())
#     smtp.quit()
#
#
# if __name__ == '__main__':
#     filepath = r"E:\PycharmProjects\pythonProject\Unittest\Calcreport.html"
#     filename = 'text_report'
#     context = '<html><h1>你好！</h1><span>以下是测试报告内容，请查收。<span><br/><span>......</span></html>'
#     subject = u'计算器自动化测试报告'
#     msg = setContext(filepath, filename, context, subject)
#
#     sender = 'dong174110@163.com'
#     recerive = '1741103252@qq.com'
#     code = 'XSJDBXNIRCFOTZVM'
#     send(msg, sender, recerive, code)

# ====================================================================================================
# !/usr/bin/env python
# -*- coding:utf-8 -*-
import yagmail


def send():
    # 连接邮箱服务器 发送方邮箱+授权码+邮箱服务地址
    yag = yagmail.SMTP(user='dong174110@163.com', password='XSJDBXNIRCFOTZVM', host='smtp.163.com')

    # 邮件正文 支持html，支持上传附件（填写在任意位置皆可）
    # 1. 上传附件
    content = ['尊敬的xxx：', '您好，以下是自动化测试报告，请查收。', '......']

    # 2. 不上传附件
    # content = ['您好，以下是自动化测试报告，请查收。']

    # 发送的几种方式 发送方+主题+内容
    # 1. 单个用户不带附件
    # yag.send('woshijieshoufang@qq.com', u'自动化测试报告', content)

    # 2. 单个用户，添加附件
    yag.send('1741103252@qq.com', u'自动化测试报告', content, r"E:\PycharmProjects\pythonProject\Unittest\Calcreport.html")

    # 3. 多个用户，多个附件
    # yag.send(['woshijieshoufang1@qq.com', 'woshijieshoufang2@163.com'], u'自动化测试报告', content,
    #          [r'E:\test\test.xlsx', r'E:\test\abc.jpg', r'E:\test\test.txt'])

    yag.close()


if __name__ == '__main__':
    send()
