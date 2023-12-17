import mysql.connector
from mysql.connector import Error

try:
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='softwarica')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor=connection.cursor()

except Error as e:
    print('Error while connecting to database',e)




def insert():
    id=int(input('Enter your id: '))
    name=input('Enter your name: ')
    address=input('Enter your address: ')
    batch=input('Enter your batch: ')

    query='insert into Student values(%s,%s,%s,%s)'
    values=(id,name,address,batch)
    cursor.execute(query,values)
    connection.commit()
    print('1 record inserted successfully')

def select():
    query='select * from Student'
    cursor.execute(query)
    records=cursor.fetchall()
    for record in records:
        print(record)

def update():
    query='update Student set Name=%s,Address=%s,Batch=%s where Id=%s'
    id=int(input('Enter id for update:'))
    name=input('Enter your name:update')
    address=input('Enter your address:update')
    batch=input('Enter your batch:update')
    values=(name,address,batch,id)
    cursor.execute(query,values)
    connection.commit()
    print('1 record Update successfully')

def delete():
    query='delete from Student where Id=%s'
    id=int(input('Enter id for delete:'))
    values=(id,)
    cursor.execute(query,values)
    connection.commit()
    print('1 record deleted sucessfully')

while True:
    print('Choose operation')
    print('1.insert\n2.select\n3.update\n4.delete')
    operation=int(input('insert value for operation'))
    if operation==1:
        insert()
    elif operation==2:
        select()
    elif operation==3:
        update()
    elif operation==4:
        delete()
    else:
        print('Invalid choice')
    option=input('Do you want to continue[y/n]')
    if option !='y':
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('Thank you ! Bye')
        break








