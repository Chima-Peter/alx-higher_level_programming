#!/usr/bin/python3
"""
Module for testing rectangle.py
"""
import unittest
from unittest.mock import patch
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
        Method to test display method
        """
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.display(), None)

    def test_str(self):
        """
        Method to test __str__ method
        """
        r1 = Rectangle(5,5,1, 2, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/2 - 5/5")

        self.assertEqual(print(r1), None)

    def test_update(self):
        """
        Method to test display method
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 10/10')

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/3')

        r1.update(height=1, width = 2, id=1)

        self.assertEqual(str(r1), '[Rectangle] (1) 10/10 - 2/1')

        r1.update(x=1, height=2, y=3, width=4, id=89)
        self.assertEqual(str(r1), '[Rectangle] (89) 1/3 - 4/2')

    def test_to_dictionary(self):
        """
        Method to test to_dictionary
        """
        r1 = Rectangle(10, 2, 1, 9, 1)
        print(r1)
        self.assertEqual(r1.to_dictionary(),\
                {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
