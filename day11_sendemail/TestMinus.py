from day11_sendemail.Calculater import Calculater
from unittest import TestCase
class TestMinus(TestCase):
    def testMinus1(self):
        a=5
        b=2
        cha=3
        calculater=Calculater()
        c=calculater.minus(a,b)
        self.assertEqual(cha,c)

    def testMinus2(self):
        a = -5
        b = 2
        cha = -7
        calculater = Calculater()
        c = calculater.minus(a, b)
        self.assertEqual(cha, c)

    def testMinus3(self):
        a = -5
        b = -2
        cha = 3
        calculater = Calculater()
        c = calculater.minus(a, b)
        self.assertEqual(cha, c)

    def testMinus4(self):
        a = 5000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002
        b = 2
        cha = 5000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        calculater = Calculater()
        c = calculater.minus(a, b)
        self.assertEqual(cha, c)

    def testMinus5(self):
        a = 0
        b = 2
        cha = -2
        calculater = Calculater()
        c = calculater.minus(a, b)
        self.assertEqual(cha, c)

    def testMinus6(self):
        a = 5
        b = 0
        cha = 5
        calculater = Calculater()
        c = calculater.minus(a, b)
        self.assertEqual(cha, c)