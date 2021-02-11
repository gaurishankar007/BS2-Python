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
        Cur.execute("insert into employee values(1001, 'John', 34), (123, 'Spidy', 35), (456, 'Bhikhari', 50);")
        # Step 5
        connection.commit();
        print('1 record inserted')

except Error as e:
    print('database connection error:', e)

finally:
    # Step 6
    if Cur:
        Cur.close()

    # Step 7
    if connection:
        connection.close()