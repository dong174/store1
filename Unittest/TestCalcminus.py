from unittest import TestCase
from Calc import  Calc


class TestCalc(TestCase):

    def testminus1(self):
        num1 = 10
        num2 = 10
        sum = 0

        calc = Calc()
        s = calc.minus(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)


    def testminus2(self):
        num1 = -10
        num2 = -10
        sum = 0

        calc = Calc()
        s = calc.minus(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testminus3(self):
        num1 = -10
        num2 = 10
        sum = -20

        calc = Calc()
        s = calc.minus(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testminus4(self):

        num1 = 100000000000000000000000000000000000000000000000000010
        num2 = 10
        sum =  100000000000000000000000000000000000000000000000000000

        calc = Calc()
        s = calc.minus(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

