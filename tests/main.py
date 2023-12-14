import unittest
from app import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator(2, 10)
        self.calc_zero = Calculator(2, 0)
        self.calc_negative = Calculator(-2, -10)

    def test_add(self):
        self.assertEqual(self.calc.add(), 12)
        self.assertIsInstance(self.calc.add(), int)

    def test_add_negative(self):
        self.assertEqual(self.calc_negative.add(), -12)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(), -8)
        self.assertIsInstance(self.calc.subtract(), int)

    def test_subtract_negative(self):
        self.assertEqual(self.calc_negative.subtract(), 8)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(), 20)
        self.assertIsInstance(self.calc.multiply(), int)

    def test_multiply_negative(self):
        self.assertEqual(self.calc_negative.multiply(), 20)

    def test_divide(self):
        self.assertEqual(self.calc.divide(), 0.2)
        self.assertIsInstance(self.calc.divide(), float)

    def test_divide_negative(self):
        self.assertEqual(self.calc_negative.divide(), 0.2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc_zero.divide()

    def test_pow(self):
        self.assertEqual(self.calc.pow(), 1024)
        self.assertIsInstance(self.calc.pow(), float)

    def test_power_negative(self):
        self.assertEqual(self.calc_negative.pow(), 0.0009765625)


if __name__ == '__main__':
    unittest.main()
