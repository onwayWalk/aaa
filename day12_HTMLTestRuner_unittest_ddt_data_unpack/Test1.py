
from ddt import ddt,data,unpack
from day11_sendemail.Calculater import Calculater
from unittest import TestCase
data_add=[
    [1,2,3],
    [-1,2,1],
    [1,-2,-1],
    [-1,-1,-2]
]
data_minus=[
    [5,4,1],
    [5, -4, 9],
    [-5, 4, -9],
    [-5, -4, -1]
]
data_mult=[
    [1,2,2],
    [-1, 2, -2],
    [-1, -2, 2],
    [1, -2, -2]
]
data_divided=[
    [6,3,2],
    [-8,-4,2],
    [-8,4,-2],
    [8,-4,-2]
]
@ddt
class TestZiCalc(TestCase):
    @data(*data_add)
    @unpack
    def testadd(self,a,b,c):
        calc = Calculater()
        s=calc.add(a,b)
        self.assertEqual(s,c)

    @data(*data_minus)
    @unpack
    def testminus(self, a, b, c):
        calc = Calculater()
        s = calc.minus(a, b)
        self.assertEqual(s, c)

    @data(*data_mult)
    @unpack
    def testmult(self, a, b, c):
        calc = Calculater()
        s = calc.multiplication(a, b)
        self.assertEqual(s, c)

    @data(*data_divided)
    @unpack
    def testdivided(self, a, b, c):
        calc = Calculater()
        s = calc.divided_by(a, b)
        self.assertEqual(s, c)


