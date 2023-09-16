#!/usr/bin/python3
"""
Module for testing rectangle.py
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Class for testing class Rectangle
    """
    def test_init(self):
        """
        Method to test class constructor for Rectangle
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(r2.id, 5)
