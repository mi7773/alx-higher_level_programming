#!/usr/bin/python3
""" test_rectangle """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ TestRectangle class """

    def test_width(self):
        """ Testing width get and set methods """

        r1 = Rectangle(1, 2, 3, 4, 5)
        r1.width = 10
        self.assertEqual(r1.width, 10)
