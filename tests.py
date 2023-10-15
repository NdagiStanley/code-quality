import unittest
from main import sum_negative, sum_positive

class SumTests(unittest.TestCase):

    def test_sum(self):
        self.assertEqual (sum_negative(-5, -5), -10)
        self.assertEqual (sum_negative(5, 2), None)

    def test_sum_positive_ok(self):
        self.assertEqual (sum_positive(2, 2), 4)
        self.assertEqual (sum_positive(-5, -2), None)
