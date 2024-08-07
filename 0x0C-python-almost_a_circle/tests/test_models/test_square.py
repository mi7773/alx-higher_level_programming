#!/usr/bin/python3
""" test_rectangle """
import unittest
from unittest.mock import patch, mock_open
from models.square import Square


class TestSquare(unittest.TestCase):
    """ TestSquare class """
    def setUp(self):
        """ Setting up the test environment """
        self.s1 = Square(1)
        self.s2 = Square(1, 2)
        self.s3 = Square(1, 2, 3)
        self.s4 = Square(1, 2, 3, 98)

    def tearDown(self):
        """ Cleaning up the test environment """
        Square.reset()

    def test_no_x(self):
        """ Testing not given x value """
        self.assertIsNotNone(self.s1)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s1.width, 1)
        self.assertEqual(self.s1.height, 1)
        self.assertEqual(self.s1.id, 1)

    def test_no_y(self):
        """ Testing not given y value """
        self.assertIsNotNone(self.s2)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s2.width, 1)
        self.assertEqual(self.s2.height, 1)
        self.assertEqual(self.s2.id, 2)

    def test_no_id(self):
        """ Testing not given id value """
        self.assertIsNotNone(self.s3)
        self.assertEqual(self.s3.x, 2)
        self.assertEqual(self.s3.y, 3)
        self.assertEqual(self.s3.width, 1)
        self.assertEqual(self.s3.height, 1)
        self.assertEqual(self.s3.id, 3)

    def test_all_is_given(self):
        """ Testing all attributes are given """
        self.assertIsNotNone(self.s4)
        self.assertEqual(self.s4.x, 2)
        self.assertEqual(self.s4.y, 3)
        self.assertEqual(self.s4.width, 1)
        self.assertEqual(self.s4.height, 1)
        self.assertEqual(self.s4.id, 98)

    def test_size_val(self):
        """ Testing the size validation """
        with self.assertRaises(TypeError):
            Square('1')
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_val(self):
        """ Testing the x validation """
        with self.assertRaises(TypeError):
            Square(1, '3')
        with self.assertRaises(ValueError):
            Square(1, -3)

    def test_y_val(self):
        """ Testing the y validation """
        with self.assertRaises(TypeError):
            Square(1, 2, '4')
        with self.assertRaises(ValueError):
            Square(1, 2, -4)

    def test_area(self):
        """ Testing the area method of the Square class """
        self.assertEqual(self.s1.area(), 1)

    def test_update(self):
        """ Testing the update method of the Square class """
        self.s4.update()
        self.assertEqual(self.s4.size, 1)
        self.s4.update(89)
        self.assertEqual(self.s4.id, 89)
        self.s4.update(89, 99)
        self.assertEqual(self.s4.size, 99)
        self.s4.update(89, 2, 100)
        self.assertEqual(self.s4.x, 100)
        self.s4.update(89, 2, 100, 4, size=7895)
        self.assertEqual(self.s4.size, 2)
        self.s4.update(*(89, 2, 3, 200))
        self.assertEqual(self.s4.x, 3)
        self.s4.update(89, 2, 3, 4)
        self.assertEqual(self.s4.y, 4)
        self.s4.update(89, 2, 3, 4, y=800)
        self.assertEqual(self.s4.y, 4)
        self.s4.update(x=800)
        self.assertEqual(self.s4.x, 800)
        self.s4.update(y=800)
        self.assertEqual(self.s4.y, 800)
        self.s4.update(x=800)
        self.assertEqual(self.s4.x, 800)
        self.s4.update(id=800)
        self.assertEqual(self.s4.id, 800)
        self.s4.update(x=789546, size=800)
        self.assertEqual(self.s4.x, 789546)
        self.s4.update(y=800, id=789)
        self.assertEqual(self.s4.id, 789)
        self.s4.update(**{'y': 800, 'id': 789})
        self.assertEqual(self.s4.id, 789)
        self.s4.update(id=789, y=800, size=1245)
        self.assertEqual(self.s4.y, 800)

    def test_str(self):
        """ Testing the str method of the rectangle class """
        self.assertEqual(str(self.s1), '[Square] (1) 0/0 - 1')

    @patch('builtins.print')
    def test_display(self, mock_print):
        """ Testing the display method of the rectangle class """
        self.s1.display()
        mock_print.assert_called_with('#\n', end='')
        self.s2.display()
        mock_print.assert_called_with('  #\n', end='')
        self.s3.display()
        mock_print.assert_called_with('\n\n\n  #\n', end='')

    def test_to_dictionary(self):
        """ Testing to_dictionary method of the square class """
        self.assertEqual(self.s1.to_dictionary(),
                         {'size': 1, 'x': 0, 'y': 0, 'id': 1})

    @patch('builtins.open', new_callable=mock_open)
    def test_save_to_file(self, mock_open):
        """ Testing save_to_file method """
        Square.save_to_file([self.s1, self.s2])
        mock_open.assert_called_with('Square.json', 'w')
        mock_open().write.assert_called_once_with('[{"x": 0, "y": 0, "id": 1, \
"size": 1}, {"x": 2, "y": 0, "id": 2, "size": 1}]')

        Square.save_to_file(None)
        mock_open.assert_called_with('Square.json', 'w')
        mock_open().write.assert_called_with('[]')

        Square.save_to_file([])
        mock_open.assert_called_with('Square.json', 'w')
        mock_open().write.assert_called_with('[]')

    def test_create(self):
        """ Testing create method """
        self.assertEqual(Square.create(**{'id': 9, 'size': 2,
                         'x': 4}).__str__(), '[Square] (9) 4/0 - 2')

    @patch('builtins.open', new_callable=mock_open,
           read_data='[{"id": 99, "size": 3}, {"id": 88, "size": 7}]')
    def test_load_from_file_success(self, mock_open):
        """ Testing load_from_file method """
        result = Square.load_from_file()
        mock_open.assert_called_with('Square.json', 'r')
        self.assertEqual(str(result[0]), '[Square] (99) 0/0 - 3')
        self.assertEqual(str(result[1]), '[Square] (88) 0/0 - 7')

    @patch('builtins.open', side_effect=Exception('error'))
    def test_load_from_file_fail(self, mock_open):
        """ Testing load_from_file method """
        result = Square.load_from_file()
        self.assertEqual(result, [])
