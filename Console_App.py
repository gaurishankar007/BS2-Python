import mysql.connector
from mysql.connector import Error
Con_Obj = None
Cur_Obj = None

try:
    Con_Obj = mysql.connector.connect(host="localhost", user='root',
                                      password="Mysql@358", database="softwarica", auth_plugin="mysql_native_password")

    if Con_Obj.is_connected():
        print("Database Connected Successfully:", Con_Obj.get_server_info())

    Cur_Obj = Con_Obj.cursor()


except Error as error:
    print("Database Connection Error: ", error)


def insert():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    batch = input("Enter Batch: ")

    query = "insert into student values(%s, %s, %s, %s);"
    values = (id, name, address, batch)
    Cur_Obj.execute(query, values)
    Con_Obj.commit()
    print("One record inserted successfully.")


def select():
    id = int(input("Enter ID: "))
    query = "select * from student where ID=%s;"
    values = (id,)
    Cur_Obj.execute(query, values)
    record = Cur_Obj.fetchone()
    print(record)


def update():
    id = int(input("Enter ID that you want to update: "))
    name = input("Enter new name: ")
    address = input("Enter new Address: ")
    batch = input("Enter new Batch: ")

    query = "update student set Name=%s, Address=%s, Batch=%s where id =%s;"
    values = (name, address, batch, id)
    Cur_Obj.execute(query, values)
    Con_Obj.commit()
    print("One record updated successfully.")


def delete():
    id = int(input("Enter ID that you want to delete: "))

    query = "delete from student where ID=%s;"
    values = (id,)
    Cur_Obj.execute(query, values)
    Con_Obj.commit()
    print("One record deleted successfully.")


print("====================================")
print("First Database Application")
print("====================================")
print("1.Insert\n2.select\n3.Update\n4.Delete")


while True:
    Option1 = int(input("Enter your operation to begin with: "))
    if Option1 == 1:
        insert()
    elif Option1 == 2:
        select()
    elif Option1 == 3:
        update()
    elif Option1 == 4:
        delete()
    else:
        print("Invalid Input.")

    Option2 = input("Do you want to continue[Y/N]: ")
    if Option2 != "Y":
        print('Thank you ! Bye')
        break
# Other example
# z = True
# while z == True:
#     a = input("Enter your name: ")
#     print(a)
#     b = input("Y/N: ")
#     if b == "N":
#         z = False

if Cur_Obj:
    Cur_Obj.close()
if Con_Obj:
    Cur_Obj.close()