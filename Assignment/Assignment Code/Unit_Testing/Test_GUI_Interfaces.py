import unittest
from Assignment_Front_End.GUI_Intearfaces import *


class TestBookInterface(unittest.TestCase):

    def setUp(self):
        pass

    def test_linear_search(self):
        self.assertEqual(True, BookInterface.linear_search([1, 4, 7, 11, 23], 11))
        self.assertEqual(False, BookInterface.linear_search([1, 4, 7, 11, 23], 13))

    def tearDown(self):
        pass


class TestAuthorBookGenreInterface(unittest.TestCase):

    def setUp(self):
        pass

    def test_bubble_sort(self):
        self.assertEqual([0, 1, 2, 3, 4, 5], AuthorBookGenreInterface.bubble_sort([4, 0, 3, 5, 2, 1]))
        self.assertEqual([7, 33, 214, 8945, 15987], AuthorBookGenreInterface.bubble_sort([214, 15987, 8945, 7, 33]))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
