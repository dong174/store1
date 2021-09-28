# import unittest
# from HTMLTestRunner import HTMLTestRunner
# import os
#
# tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")
#
#
#
# runner  = HTMLTestRunner.HTMLTestRunner(
#     title = "参数化测试报告",
#     description="ICBC测试报告",
#     verbosity=1,
#     stream=open(file="ICBC.html",mode="w+",encoding="utf-8")
# )
#
# runner.run(tests)


import os
import yagmail
from HTMLTestRunner import HTMLTestRunner
import  unittest

tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")



runner  = HTMLTestRunner.HTMLTestRunner(
    title = "ICBC测试报告",
    #description="加法测试报告",
    verbosity=1,
    stream=open(file="ICBC.html",mode="w+",encoding="utf-8")
)

runner.run(tests)

def send():
    # 连接邮箱服务器 发送方邮箱+授权码+邮箱服务地址
    yag = yagmail.SMTP(user='dong174110@163.com', password='XSJDBXNIRCFOTZVM', host='smtp.163.com')
    content = ['您好，这里是董伟的参数化测试报告，请查收。', '......']
    yag.send('13552648187@163.com', u'自动化测试报告', content, [r"E:\PycharmProjects\pythonProject\参数化测试\ICBC.html" ,r"E:\PycharmProjects\pythonProject\参数化测试\银行.xlsx"])
    yag.close()


if __name__ == '__main__':
    # while True:
    send()
#
#
#
#
#
#
#
#
