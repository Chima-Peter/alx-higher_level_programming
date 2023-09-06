#!/usr/bin/python3
"""
Writing unittest for 6-max_integer
"""
import unittest
max_int = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Testing max_integer
    """
    def test_max_integer(self):
        """
        Writing test for max_integer
        """
        self.assertEqual(max_int([1, 8, 4]), 8)
        self.assertEqual(max_int([-3, -4, -1]), -1)
        self.assertRaises(TypeError, max_int, "string")
        self.assertRaises(TypeError, max_int, [1, 2, '4'])
        self.assertEqual(max_int(), None)
        self.assertEqual(max_int([]), None)
