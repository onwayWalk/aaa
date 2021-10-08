from day11_sendemail.Calculater import  Calculater
from unittest import  TestCase

class TestDivided_by(TestCase):
    def testDiv1(self):
        a=4
        b=2
        value=2
        calculater=Calculater()
        r=calculater.divided_by(a,b)
        self.assertEqual(value,r)

    def testDiv2(self):
        a=-4
        b=2
        value=-2
        calculater=Calculater()
        r=calculater.divided_by(a,b)
        self.assertEqual(value,r)
    def testDiv3(self):
        a=4
        b=-2
        value=-2
        calculater=Calculater()
        r=calculater.divided_by(a,b)
        self.assertEqual(value,r)
    def testDiv4(self):
        a=-4
        b=-2
        value=2
        calculater=Calculater()
        r=calculater.divided_by(a,b)
        self.assertEqual(value,r)