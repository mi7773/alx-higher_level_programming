import unittest
from models.base import Base
""" test_base """


class TestBase(unittest.TestCase):
    """ TestBaseClass class """

    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
