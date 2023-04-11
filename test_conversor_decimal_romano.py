import unittest
from conversor_decimal_romano import conversor_decimal_romano
class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = conversor_decimal_romano(1)
        self.assertEqual(resultado, "I")
    def test_IV(self):
        resultado = conversor_decimal_romano(4)
        self.assertEqual(resultado, "IV")
    def test_V(self):
        resultado = conversor_decimal_romano(5)
        self.assertEqual(resultado, "V")
    def test_IX(self):
        resultado = conversor_decimal_romano(9)
        self.assertEqual(resultado, 'IX')
    def test_X(self):
        resultado = conversor_decimal_romano(10)
        self.assertEqual(resultado, 'X')
    def test_XL(self):
        resultado = conversor_decimal_romano(40)
        self.assertEqual(resultado, 'XL')
    def test_L(self):
        resultado = conversor_decimal_romano(50)
        self.assertEqual(resultado, 'L')
    def test_C(self):
        resultado = conversor_decimal_romano(100)
        self.assertEqual(resultado, 'C')
    def test_496(self):
        resultado = conversor_decimal_romano(496)
        self.assertEqual(resultado, 'CDXCVI')
    def test_D(self):
        resultado = conversor_decimal_romano(500)
        self.assertEqual(resultado, 'D')
    def test_626(self):
        resultado = conversor_decimal_romano(626)
        self.assertEqual(resultado, 'DCXXVI')
    def test_894(self):
        resultado = conversor_decimal_romano(894)
        self.assertEqual(resultado, 'DCCCXCIV')
    def test_M(self):
        resultado = conversor_decimal_romano(1000)
        self.assertEqual(resultado, 'M')

if __name__ == '__main__':
    unittest.main()
    