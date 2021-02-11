import mysql.connector
from mysql.connector import Error


class DbConnection:
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost", user="root",
                                           password="Mysql@358", database="student_management_system",
                                           auth_plugin="mysql_native_password")
        self.cur = self.con.cursor()

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
        self.con.commit()
        return records
    