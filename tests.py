import unittest
from main import sum_negative, sum_positive

class SumTests(unittest.TestCase):

    def test_sum_negative_ok(self):
        self.assertEqual (sum_negative(-5, -5), -10)
        self.assertEqual (sum_negative(5, 5), None)
        self.assertEqual (sum_negative(5, -2), None)
        self.assertEqual (sum_negative(-5, 2), None)
        self.assertEqual (sum_negative(0, 0), None)

    def test_sum_positive_ok(self):
        self.assertEqual (sum_positive(2, 2), 4)
        self.assertEqual (sum_positive(-2, -2), None)
        self.assertEqual (sum_positive(2, -2), None)
        self.assertEqual (sum_positive(-2, 2), None)
        self.assertEqual (sum_positive(0, 0), None)
