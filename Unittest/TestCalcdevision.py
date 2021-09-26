from unittest import TestCase
from Calc import  Calc


class TestCalc(TestCase):

    def testde1(self):
        num1 = 21
        num2 = 10
        sum = 2.1

        calc = Calc()
        s = calc.devision(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)


    def testde2(self):
        num1 = -10
        num2 = -10
        sum = 1

        calc = Calc()
        s = calc.devision(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testde3(self):
        num1 = -10
        num2 = 10
        sum = -1

        calc = Calc()
        s = calc.devision(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testde4(self):

        num1 = 100000000000000000000000000000000000000000000000000000
        num2 = 10
        sum =  10000000000000000000000000000000000000000000000000000

        calc = Calc()
        s = calc.devision(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)