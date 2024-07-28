#!/usr/bin/python3
""" test_base """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ TestBase class """

    def setUp(self):
        """ Setting up the test environment """
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(456)

    def tearDown(self):
        """ Cleaning up the test environment """
        Base.reset()

    def test_id_auto_assign(self):
        """ Testing id automatic assignment """
        self.assertEqual(self.b1.id, 1)

    def test_id_increment(self):
        """ Testing id increment """
        self.assertEqual(self.b2.id, 2)

    def test_id_manual_assign(self):
        """ Testing id manual assignment """
        self.assertEqual(self.b3.id, 456)
