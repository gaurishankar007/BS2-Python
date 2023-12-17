import mysql.connector
from mysql.connector import Error


class DbConnection:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user="root",
                                               password="Mysql@358", database="book_management_system",
                                               auth_plugin="mysql_native_password")
            if self.con.is_connected():
                print("Database connected successfully: ", self.con.get_server_info())

            self.cur = self.con.cursor()
        except Error as error:
            print("Database connection error: ", error)

    def add(self, query, values):
        self.cur.execute(query, values)
        self.con.commit()

    def update(self, query, values):
        self.cur.execute(query, values)
        self.con.commit()

    def delete(self, query, values):
        self.cur.execute(query, values)
        self.con.commit()

    def select(self, query):
        self.cur.execute(query)
        records = self.cur.fetchall()
        return records

    def search(self, query, values):
        self.cur.execute(query, values)
        records = self.cur.fetchall()
        return records

    def close(self):
        if self.cur:
            self.cur.close()
        if self.con:
            self.cur.close()




