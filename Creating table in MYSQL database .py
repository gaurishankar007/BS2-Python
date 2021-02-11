import mysql.connector
# Creating the connection object
connection = mysql.connector.connect(host="localhost", user="root",
                                     password='Mysql@358', database="algorithm", auth_plugin='mysql_native_password')
# Creating the cursor object
cur = connection.cursor()
# executing the query
cur.execute('Create table if not exists Employee(id int, name varchar(20), Age int);')
# Committing
connection.commit()
print("Table created successfully")
cur.close()
# Close the connection
connection.close()