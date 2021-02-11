# Step 1
import mysql.connector
from mysql.connector import Error
connection = None
Cur = None
try:
    # Step 2
    connection = mysql.connector.connect(host="localhost", user="root",
                                         password="Mysql@358", database='algorithm', auth_plugin="mysql_native_password")
    if connection.is_connected():
        db_info = connection.get_server_info()
        print('Database information:', db_info)

        # Step 3
        Cur = connection.cursor();
        # Step 4
        Cur.execute("select * from employee;")
        # Fetch only one time
        print(Cur.fetchone())
        print(Cur.fetchall())
        print(Cur.fetchmany(2))
        # Printing each record row by row
        records = Cur.fetchall()
        for i in records:
            print(i)

        # Step 5
        connection.commit();


except Error as e:
    print('database connection error:', e)

finally:
    # Step 6
    if Cur:
        Cur.close()

    # Step 7
    if connection:
        connection.close()