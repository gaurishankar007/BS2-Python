import unittest
from Assignment_Model.Get_Set_Methods import *


class TestBookDelete(unittest.TestCase):

    def setUp(self):
        self.ref = BookDelete("1015478965")

    def test_set_isbn(self):
        self.ref.set_isbn("4879651234")
        self.assertEqual("4879651234", self.ref.get_isbn())

    def test_get_isbn(self):
        self.assertEqual("1015478965", self.ref.get_isbn())

    def tearDown(self):
        self.lgn = None


class TestBookGenreAddUpdate(unittest.TestCase):

    def setUp(self):
        self.ref = BookGenreAddUpdate("6", "Horror", "5")

    def test_set_book_genre_name(self):
        self.ref.set_book_genre_name("Biography")
        self.assertEqual("Biography", self.ref.get_book_genre_name())

    def test_get_book_genre_name(self):
        self.assertEqual("Horror", self.ref.get_book_genre_name())

    def tearDown(self):
        self.ref = None


if __name__ == '__main__':
    unittest.main()
