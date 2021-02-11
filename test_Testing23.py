import unittest
from Testing_Sample import *


class TestInterface(unittest.TestCase):

    def setUp(self):
        self.ab = Interface()

    def test_add(self):
        self.assertEqual(5, self.ab.add(2, 3))
        self.assertEqual(4, self.ab.add(-1, 5))
        self.assertEqual(-15, self.ab.add(-7, -8))

    def test_divide(self):
        self.assertEqual(2, self.ab.divide(8, 4))

    def tearDown(self):
        self.ab = None


if __name__ == '__main__':
    unittest.main()