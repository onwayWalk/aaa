
from day11_sendemail.Calculater import Calculater
from unittest import  TestCase
class TestAdd(TestCase):
    def testadd1(self):
        a=1
        b=2
        sum=3
        c = Calculater()
        s=c.add(a,b)
        self.assertEqual(sum,s)
    def testadd2(self):
        a = -1
        b = 2
        sum = 1
        calculater = Calculater()
        s = calculater.add(a, b)
        self.assertEqual(sum, s)
    def testadd3(self):
        a = -1
        b = -2
        sum =- 3
        calc = Calculater()
        s = calc.add(a, b)
        self.assertEqual(sum, s)
    def testadd4(self):
        a = 0
        b = -2
        sum = -2
        calculater = Calculater()
        s = calculater.add(a, b)
        self.assertEqual(sum, s)
