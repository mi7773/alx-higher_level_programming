#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)
        self.assertEqual(max_integer([1, 2, 8, 4]), 8)
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([1.5, 1.3, 1.2, 1.1]), 1.5)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertRaises(TypeError, max_integer, [], [])
        self.assertEqual(max_integer(['a', 'b', 'c', 'a']), 'c')
        self.assertEqual( max_integer([[1, 2],[1, 1, 1, 1, 3]]), [1, 2])
        with self.assertRaises(TypeError):
            max_integer([], [])
