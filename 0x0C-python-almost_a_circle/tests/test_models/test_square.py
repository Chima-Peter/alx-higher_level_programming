#!/usr/bin/python3
"""
Module for testing square.py
"""
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """
    Class for testing Square
    """
    def test_init(self):
        """
        Testing first method
        """
        s1 = Square(5)
        print(s1)
        self.assertEqual(s1.area(), 25)

        s2 = Square(2, 2, 0, 2)
        print(s2)
        self.assertEqual(str(s2), '[Square] (2) 2/0 - 2')

        s1 = Square(5)
        s1.size = 8
        self.assertEqual(s1.size, 8)

        with self.assertRaises(TypeError):
            s1.size("9")
