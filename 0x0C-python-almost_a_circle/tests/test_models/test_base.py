#!/usr/bin/python3
""" test_base """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ TestBase class """

    def setUp(self):
        """ Setting up the test environment """

    def tearDown(self):
        """ Cleaning up the test environment """

    def test_id_auto_assign(self):
        """ Testing id automatic assignment """
        self.assertEqual(Base().id, 1)

    def test_id_increment(self):
        """ Testing id increment """
        self.assertEqual(Base().id, 2)

    def test_id_manual_assign(self):
        """ Testing id manual assignment """
        self.assertEqual(Base(88).id, 88)
