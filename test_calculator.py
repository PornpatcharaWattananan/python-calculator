import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(12, 8), 20)
    
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-15, 7), -8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(20, 10), 10)
        self.assertEqual(self.calc.subtract(18, 25), -7)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(6, 5), 30)
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(36, 9), 4)
        self.assertEqual(self.calc.divide(21, 4), 5)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(50, 7), 1)
    
    def test_modulo_zero(self):
        self.assertEqual(self.calc.modulo(38, 6), 2)

if __name__ == '__main__':
    unittest.main()
