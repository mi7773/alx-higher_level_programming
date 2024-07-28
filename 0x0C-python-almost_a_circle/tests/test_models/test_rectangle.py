#!/usr/bin/python3
""" test_rectangle """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ TestRectangle class """

    def test_x_opt_val(self):
        """ Testing x optional value """

        self.assertEqual(Rectangle(1, 2).x, 0)

    def test_y_opt_val(self):
        """ Testing y optional value """

        self.assertEqual(Rectangle(1, 2).y, 0)
