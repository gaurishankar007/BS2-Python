import unittest
from Assignment_Back_End.Connector import *


class TestDbConnection(unittest.TestCase):
    def setUp(self):
        self.ref = DbConnection()

    def test_update(self):
        query = "update books set Book_Title=%s, Language=%s, Author_ID=%s, Book_Genre_ID=%s, " \
                "Publication_Year=%s, Price=%s, No_Of_Copies=%s where ISBN=%s;"
        values = ("Avenger", "English", 3, 1, "2019", "Rs.1500", "10", "9816349292")
        self.ref.update(query, values)
        expect = [("9816349292", "Avenger", "English", 3, 1, "2019", "Rs.1500", "10")]

        query1 = "select * from books where Book_Title=%s;"
        values1 = ("Avenger",)
        actual = self.ref.search(query1, values1)
        self.assertEqual(expect, actual)

    def test_select(self):
        self.assertEqual([('1012456982', 'MadMax', 'English', 1, 2, '2015', 'Rs.1600', '10')],
                         self.ref.select("select * from books where ISBN='1012456982';"))

    def test_search(self):
        self.assertEqual([(1, 'Laxmi', 'Debkota', '5')],
                         self.ref.search("select * from authors where Author_ID=%s;", (1, )))

    def tearDown(self):
        self.ref.close()
        self.ref = None


if __name__ == '__main__':
    unittest.main()
