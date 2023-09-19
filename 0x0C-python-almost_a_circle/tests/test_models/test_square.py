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

    def test_update(self):
        """
        Tests update method
        """
        s1 = Square(5, 0, 0, 1)
        s1.update(10)
        self.assertEqual(str(s1), '[Square] (10) 0/0 - 5')

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), '[Square] (1) 3/0 - 2')

        s1.update(size=7, y=1, x=12)
        self.assertEqual(str(s1), '[Square] (1) 12/1 - 7')
