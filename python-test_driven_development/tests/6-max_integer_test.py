#!/usr/bin/python3
"""Task 6"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class for testing function"""
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 4, 3, 1]), 4)
        self.assertEqual(max_integer([1, 4, -3, 1]), 4)
        self.assertEqual(max_integer([-1, -4, -3, -1]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
