import unittest
from Calc import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertAlmostEqual(self.calc.divide(6, 3), 2.0)

    def test_divide_float(self):
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)


if __name__ == '__main__':
    unittest.main()