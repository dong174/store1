
from HTMLTestRunner import HTMLTestRunner
import unittest

tests = unittest.defaultTestLoader.discover(r"E:\PycharmProjects\pythonProject\Unittest",pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(

    title = "计算器测试报告",
    description = "加减乘除测试报告",
    verbosity = 1,
    stream = open(file='Calcreport.html',mode='w+',encoding="utf-8")

)

runner.run(tests)









