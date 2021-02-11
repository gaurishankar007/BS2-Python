# Step-1 import the necessary db api module
import mysql.connector
from mysql.connector import Error
Con_Obj = None
Cur_Obj = None

# Step-2 Creating the connection object
try:
    Con_Obj = mysql.connector.connect(host="localhost", user="root",
                                         password="Mysql@358", database="algorithm", auth_plugin="mysql_native_password")
    if Con_Obj.is_connected():
        print("Database Successfully Connected.")
        print("Database Information:", Con_Obj.get_server_info())

# Step-3 Creating the cursor object
    Cur_Obj = Con_Obj.cursor()

# step_4 Executing the cursor object
    id = int(input("Enter the employee id: "))
    name = input("Enter the employee name: ")
    age = int(input("Enter the employee age: "))
    query = "Insert into employee values(%s, %s, %s);"
    values = (id, name, age)
    Cur_Obj.execute(query, values)

# Step-5 Save the changes
    Con_Obj.commit()
    print("One record inserted successfully")

except Error as error:
    print("Database Connection Error:", error)

finally:
    # Step-6 Closing the cursor and connection
    if Cur_Obj:
        Cur_Obj.close()
    if Con_Obj:
        Con_Obj.close()