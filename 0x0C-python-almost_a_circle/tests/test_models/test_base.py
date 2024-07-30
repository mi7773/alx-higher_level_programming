#!/usr/bin/python3
""" test_base """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import patch, mock_open


class TestBase(unittest.TestCase):
    """ TestBase class """

    def setUp(self):
        """ Setting up the test environment """
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(456)
        self.r1 = Rectangle(1, 2)
        self.s1 = Square(1)

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

    def test_to_json_string(self):
        """ Testing to_json_string method """
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{'a': 1, 'b': 2, 'c': False}]),
                         '[{"a": 1, "b": 2, "c": false}]')

    @patch('builtins.open', new_callable=mock_open)
    def test_save_to_file(self, mock_open):
        """ Testing save_to_file method """
        Rectangle.save_to_file([self.r1, self.s1])
        mock_open.assert_called_with('Rectangle.json', 'w')
        mock_open().write.assert_called_once_with('[{"x": 0, "y": 0, "id": 4, \
"height": 2, "width": 1}, {"x": 0, "y": 0, "id": 5, "size": 1}]')
