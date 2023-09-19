#!/usr/bin/python3
"""
Test Class for BASE class
"""
import unittest
from models.base import Base

class TestBase:
    """
    The test case for BASE class
    Args:
        test__init__
    """

    def test_init(self):
        """
        Tests the class constructor
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(10)
        self.assertEqual(b2.id, 10)
