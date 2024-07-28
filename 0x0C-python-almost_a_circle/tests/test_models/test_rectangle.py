#!/usr/bin/python3
""" test_rectangle """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ TestRectangle class """

    def test_no_x(self):
        """ Testing not given x value """

        self.assertIsNotNone(Rectangle(1, 2))

    def test_no_y(self):
        """ Testing not given y value """

        self.assertIsNotNone(Rectangle(1, 2, 3))

    def test_no_id(self):
        """ Testing not given id value """

        self.assertIsNotNone(Rectangle(1, 2, 3, 4))
