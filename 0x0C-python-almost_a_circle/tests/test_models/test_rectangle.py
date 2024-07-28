#!/usr/bin/python3
""" test_rectangle """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ TestRectangle class """

    def setUp(self):
        """ Setting up the test environment """
        self.r1 = Rectangle(1, 2)
        self.r2 = Rectangle(1, 2, 3)
        self.r3 = Rectangle(1, 2, 3, 4)


    def tearDown(self):
        """ Cleaning up the test environment """
        Rectangle.reset()

    def test_no_x(self):
        """ Testing not given x value """

        self.assertIsNotNone(self.r1)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.id, 1)

    def test_no_y(self):
        """ Testing not given y value """

        self.assertIsNotNone(self.r2)
        self.assertEqual(self.r2.x, 3)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.id, 2)

    def test_no_id(self):
        """ Testing not given id value """

        self.assertIsNotNone(self.r3)
        self.assertEqual(self.r3.x, 3)
        self.assertEqual(self.r3.y, 4)
        self.assertEqual(self.r3.width, 1)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r3.id, 3)
