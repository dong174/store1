from unittest import TestCase
from Calc import  Calc


class TestCalc(TestCase):

    def testmu1(self):
        num1 = 10
        num2 = 10
        sum = 100

        calc = Calc()
        s = calc.multi(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)


    def testmu2(self):
        num1 = -10
        num2 = -10
        sum = 100

        calc = Calc()
        s = calc.multi(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testmu3(self):
        num1 = -10
        num2 = 10
        sum = -100

        calc = Calc()
        s = calc.multi(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testmu4(self):

        num1 = 100000000000000000000000000000000000000000000000000000
        num2 = 10
        sum = 1000000000000000000000000000000000000000000000000000000

        calc = Calc()
        s = calc.multi(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)