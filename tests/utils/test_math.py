import unittest


from mypackage.utils import math


class TestAverage(unittest.TestCase):
    def test_valid_input(self):
        a = math.average(5, 7, 8)
        self.assertAlmostEqual((5+7+8)/3.0, a)

    def test_invalid_input(self):
        with self.assertRaises(ValueError) as _:
            math.average(5, 7, '9')

    def test_no_input(self):
        with self.assertRaises(ValueError) as _:
            math.average()


class TestMedian(unittest.TestCase):
    def test_valid_input_odd(self):
        a = math.median(1, 3, 7)
        self.assertAlmostEqual(3, a)

    def test_valid_input_even(self):
        a = math.median(1, 3, 4, 100)
        self.assertAlmostEqual(3.5, a)

    def test_invalid_input(self):
        with self.assertRaises(ValueError) as _:
            math.average(5, 7, '9')

    def test_no_input(self):
        with self.assertRaises(ValueError) as _:
            math.average()
