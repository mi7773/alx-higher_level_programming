#!/usr/bin/python3
""" test_base """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ TestBase class """

    def test_id_automatic_assignment(self):
        """ Testing id """
        self.assertEqual(Base().id, 1)

    def test_id_increment(self):
        """ Testing id increment """
        self.assertEqual(Base().id, 2)

    def test_id_manual_assignment(self):
        """ Testing id """
        self.assertEqual(Base(99).id, 99)
