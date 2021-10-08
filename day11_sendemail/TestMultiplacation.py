from day11_sendemail.Calculater import Calculater
from unittest import TestCase

class TestMultiplacation(TestCase):
    def testMult1(self):
        a = 2
        b = 4
        value = 8
        cal = Calculater()
        r=cal.multiplication(a, b)
        self.assertEqual(value, r)

    def testMult2(self):
        a = -2
        b = -4
        value = 8
        cal = Calculater()
        r = cal.multiplication(a, b)
        self.assertEqual(value, r)

    def testMult3(self):
        a = -2
        b = 4
        value = -8
        cal = Calculater()
        r = cal.multiplication(a, b)
        self.assertEqual(value, r)

    def testMult4(self):
        a = 2
        b = 0
        value = 0
        cal = Calculater()
        r = cal.multiplication(a, b)
        self.assertEqual(value, r)
    