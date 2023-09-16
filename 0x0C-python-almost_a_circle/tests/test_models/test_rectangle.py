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
        r1 = Rectangle(10, 2, 0, 0, 1)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(r2.id, 5)

    def test_fail(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(TypeError):
            Rectangle("10", 5)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.height = 0
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "3", 4)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.x = -10
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 8, "4")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.y = -10

    def test_area(self):
        """
        Method to test area of a rectangle
        """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r1 = Rectangle(3, 3, 0, 0)
        self.assertEqual(r1.area(), 9)

        with self.assertRaises(ValueError):
            r1 = Rectangle(3, 0)
            r1.area()

        with self.assertRaises(TypeError):
            r1 = Rectangle(3, "2")
            r1.area()

        def test_display(self):
            """
            Method to test display methid
            """
            r1 = Rectangle(1, 1)
            self.assertEqual(r1.display(), '#')
