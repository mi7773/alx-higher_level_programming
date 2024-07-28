#!/usr/bin/python3
""" test_base """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ TestBase class """

    def test_id(self):
        """ Testing id """
        b1 = Base()
        self.assertEqual(b1.id, 1)
