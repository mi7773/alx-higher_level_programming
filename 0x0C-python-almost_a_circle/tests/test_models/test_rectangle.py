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
        self.r4 = Rectangle(1, 2, 3, 4, 5)

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

    def test_all_is_given(self):
        """ Testing all attributes are given """
        self.assertIsNotNone(self.r4)
        self.assertEqual(self.r4.x, 3)
        self.assertEqual(self.r4.y, 4)
        self.assertEqual(self.r4.width, 1)
        self.assertEqual(self.r4.height, 2)
        self.assertEqual(self.r4.id, 5)

    def test_width_val(self):
        """ Testing the width validation """
        with self.assertRaises(TypeError):
            Rectangle('1', 2)
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_val(self):
        """ Testing the height validation """
        with self.assertRaises(TypeError):
            Rectangle(1, '2')
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_x_val(self):
        """ Testing the x validation """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, '3')
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_y_val(self):
        """ Testing the y validation """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, '4')
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """ Testing the area method of the Rectangle class """
        self.assertEqual(self.r1.area(), 2)

    def test_update(self):
        """ Testing the update method of the Rectangle class """
        self.r4.update()
        self.assertEqual(self.r4.width, 1)
        self.r4.update(89)
        self.assertEqual(self.r4.id, 89)
        self.r4.update(89, 99)
        self.assertEqual(self.r4.width, 99)
        self.r4.update(89, 2, 100)
        self.assertEqual(self.r4.height, 100)
        self.r4.update(89, 2, 3, 200)
        self.assertEqual(self.r4.x, 200)
        self.r4.update(89, 2, 3, 4, 500)
        self.assertEqual(self.r4.y, 500)

    def test_str(self):
        """ Testing the str method of the rectangle class """
        self.assertEqual(str(self.r1), '[Rectangle] (1) 0/0 - 1/2')

    def test_display(self):
        """ Testing the display method of the rectangle class """
