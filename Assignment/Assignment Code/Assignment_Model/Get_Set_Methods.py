class Login:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password


class BookADDUpdate:
    def __init__(self, isbn, book_title, language, author_id, book_genre_id, publication_year, price, no_of_copies):
        self.__isbn = isbn
        self.__book_title = book_title
        self.__language = language
        self.__author_id = author_id
        self.__book_genre_id = book_genre_id
        self.__publication_year = publication_year
        self.__price = price
        self.__no_of_copies = no_of_copies

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn

    def set_book_title(self, book_title):
        self.__book_title = book_title

    def get_book_title(self):
        return self.__book_title

    def set_language(self, language):
        self.__language = language

    def get_language(self):
        return self.__language

    def set_author_id(self, author_id):
        self.__author_id = author_id

    def get_author_id(self):
        return self.__author_id

    def set_book_genre_id(self, book_genre_id):
        self.__book_genre_id = book_genre_id

    def get_book_genre_id(self):
        return self.__book_genre_id

    def set_publication_year(self, publication_year):
        self.__publication_year = publication_year

    def get_publication_year(self):
        return self.__publication_year

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_no_of_copies(self, no_of_copies):
        self.__no_of_copies = no_of_copies

    def get_no_of_copies(self):
        return self.__no_of_copies


class BookDelete:
    def __init__(self, isbn):
        self.__isbn = isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn


class AuthorAddUpdate:
    def __init__(self, author_id, author_first_name, author_last_name, no_of_books):
        self.__author_id = author_id
        self.__author_first_name = author_first_name
        self.__author_last_name = author_last_name
        self.__no_of_books = no_of_books

    def set_author_id(self, author_id):
        self.__author_id = author_id

    def get_author_id(self):
        return self.__author_id

    def set_author_first_name(self, author_first_name):
        self.__author_first_name = author_first_name

    def get_author_first_name(self):
        return self.__author_first_name

    def set_author_last_name(self, author_last_name):
        self.__author_last_name = author_last_name

    def get_author_last_name(self):
        return self.__author_last_name

    def set_no_of_books(self, no_of_books):
        self.__no_of_books = no_of_books

    def get_no_of_books(self):
        return self.__no_of_books


class AuthorDelete:
    def __init__(self, author_id):
        self.__author_id = author_id

    def set_author_id(self, author_id):
        self.__author_id = author_id

    def get_author_id(self):
        return self.__author_id


class BookGenreAddUpdate:
    def __init__(self, book_genre_id, book_genre_name, no_of_books):
        self.__book_genre_id = book_genre_id
        self.__book_genre_name = book_genre_name
        self.__no_of_books = no_of_books

    def set_book_genre_id(self, book_genre_id):
        self.__book_genre_id = book_genre_id

    def get_book_genre_id(self):
        return self.__book_genre_id

    def set_book_genre_name(self, book_genre_name):
        self.__book_genre_name = book_genre_name

    def get_book_genre_name(self):
        return self.__book_genre_name

    def set_no_of_books(self, no_of_books):
        self.__no_of_books = no_of_books

    def get_no_of_books(self):
        return self.__no_of_books


class BookGenreDelete:
    def __init__(self, book_genre_id):
        self.__book_genre_id = book_genre_id

    def set_book_genre_id(self, book_genre_id):
        self.__book_genre_id = book_genre_id

    def get_book_genre_id(self):
        return self.__book_genre_id

