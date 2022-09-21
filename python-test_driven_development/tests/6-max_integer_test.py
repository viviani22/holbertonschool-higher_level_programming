#!/usr/bin/python3
"""Task 6"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class for testing function"""
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([float('inf'), 2, 3]), inf)


    def test_types(self):
        self.assertRaises(TypeError, max_integer, [1, 'sup'])
        self.assertRaises(TypeError, max_integer, [float('NaN'), 'sup'])
