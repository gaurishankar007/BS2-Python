from tkinter import *
from tkinter import messagebox

import mysql.connector
from mysql.connector import Error
con = None
cur = None

try:
    con = mysql.connector.connect(host="localhost", user="root",
                                  password="Mysql@358", database="19a_assignment", auth_plugin="mysql_native_password")

    if con.is_connected():
        print("Database connected successfully: ", con.get_server_info())

    cur = con.cursor()

except Error as error:
    print("Database connection error: ", error)

else:
    def add():
        if Ent_id.get() == "" or Ent_name.get() == "" or Ent_Address.get() == "" or Ent_Age.get() == "":
            messagebox.showerror("Unfulfilled Boxes", "Please fill all the boxes first!")
        else:
            id = Ent_id.get()
            name = Ent_name.get()
            address = Ent_Address.get()
            age = Ent_Age.get()

            query = "insert into information values(%s, %s, %s, %s);"
            values = (int(id), name, address, int(age))
            cur.execute(query, values)
            con.commit()
            messagebox.showinfo("Data Added Successful", "One data is successfully added.")


    def update():
        query = "select * from Information;"
        cur.execute(query)
        records = cur.fetchall()
        id_list = []
        for i in records:
            id_list.append(i[0])

        if Ent_id.get() == "":
            messagebox.showerror("Unfulfilled ID", "you must enter the ID to update!")
        elif int(Ent_id.get()) not in id_list:
            messagebox.showerror("Unknown ID", "No such ID in database!")
        else:
            id = Ent_id.get()
            name = Ent_name.get()
            address = Ent_Address.get()
            age = Ent_Age.get()

            query = "Update information set Name=%s, Address=%s, Age=%s where ID=%s;"
            values = (name, address, int(age), int(id))
            cur.execute(query, values)
            con.commit()
            messagebox.showinfo("Data Updated Successful", "One data is successfully updated.")


    def delete():
        query = "select * from Information;"
        cur.execute(query)
        records = cur.fetchall()
        id_list = []
        for i in records:
            id_list.append(i[0])

        if Ent_id.get() == "":
            messagebox.showerror("Unfulfilled ID", "you must enter the ID to delete!")
        elif int(Ent_id.get()) not in id_list:
            messagebox.showerror("Unknown ID", "No such ID in database!")
        else:
            id = int(Ent_id.get())

            query = "delete from information where ID=%s"
            values = (id,)
            cur.execute(query, values)
            con.commit()
            messagebox.showinfo("Data Deleted Successful", "One data is successfully deleted.")


    def clear():
        Ent_id.delete(0, END)
        Ent_name.delete(0, END)
        Ent_Address.delete(0, END)
        Ent_Age.delete(0, END)


    # Creating Window
    Window = Tk()
    Window.title("Personal Information Application")
    Window.geometry("600x500+700+150")

    # ============================Heading============================
    Heading = Label(Window, text="Personal Information Application",
                    font=('cambria', 20, 'bold'), bg="orange", bd=5, relief=GROOVE)
    Heading.pack(side=TOP, fill=X)  # fill fills the label fully horizontally and vertically

    # =============================Frame=============================
    Main_Frame = Frame(Window, bg='blue', bd=7, relief=RIDGE)
    Main_Frame.place(x=50, y=45, width=500, height=270)  # Putting width and height in place fixes the frame size

    Btn_Frame = Frame(Window, bg="green", bd=7, relief=RIDGE)
    Btn_Frame.place(x=50, y=350, width=500, height=100)

    # =================Adding Widget in Main_Frame====================
    Lbl_id = Label(Main_Frame, text="ID", bg="orange", font=("cambria", 15, "bold"), width=10, bd=5, relief=GROOVE)
    Lbl_id.grid(row=0, column=0, padx=10, pady=15)

    Ent_id = Entry(Main_Frame, font=("cambria", 15, "bold"), bd=4, relief=SUNKEN)
    Ent_id.grid(row=0, column=1)

    Lbl_name = Label(Main_Frame, text="Name", bg="orange", font=("cambria", 15, "bold"), width=10, bd=5, relief=GROOVE)
    Lbl_name.grid(row=1, column=0, padx=10, pady=15)

    Ent_name = Entry(Main_Frame, font=("cambria", 15, "bold"), bd=4, relief=SUNKEN)
    Ent_name.grid(row=1, column=1)

    Lbl_Address = Label(Main_Frame, text="Address", bg="orange", font=("cambria", 15, "bold"), width=10, bd=5, relief=GROOVE)
    Lbl_Address.grid(row=2, column=0, padx=10, pady=15)

    Ent_Address = Entry(Main_Frame, font=("cambria", 15, "bold"), bd=4, relief=SUNKEN)
    Ent_Address.grid(row=2, column=1)

    Lbl_Age = Label(Main_Frame, text="Age", bg="orange", font=("cambria", 15, "bold"), width=10, bd=5, relief=GROOVE)
    Lbl_Age.grid(row=3, column=0, padx=10, pady=15)

    Ent_Age = Entry(Main_Frame, font=("cambria", 15, "bold"), bd=4, relief=SUNKEN)
    Ent_Age.grid(row=3, column=1)

    # =====================Buttons on Btn_Frame========================
    btn_add = Button(Btn_Frame, text="Add", font=("cambria", 20, "normal"),
                     bg="orange", bd=4, relief=GROOVE, command=add)
    btn_add.pack(side=LEFT, padx=15)

    btn_update = Button(Btn_Frame, text="Update", font=("cambria", 20, "normal"),
                        bg="orange", bd=4, relief=GROOVE, command=update)
    btn_update.pack(side=LEFT, padx=15)

    btn_delete = Button(Btn_Frame, text="Delete", font=("cambria", 20, "normal"),
                        bg="orange", bd=4, relief=GROOVE, command=delete)
    btn_delete.pack(side=LEFT, padx=15)

    btn_clear = Button(Btn_Frame, text="Clear", font=("cambria", 20, "normal"),
                       bg="orange", bd=4, relief=GROOVE, command=clear)
    btn_clear.pack(side=LEFT, padx=15)

    Window.mainloop()

finally:
    if cur:
        cur.close()

    if con:
        con.close()