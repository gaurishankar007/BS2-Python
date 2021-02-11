from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import mysql.connector
from mysql.connector import Error

con = None
cur = None

try:
    con = mysql.connector.connect(host="localhost", user="root",
                                  password="Mysql@358", database="student_management_system", auth_plugin="mysql_native_password")

    if con.is_connected():
        print("Database connected successfully: ", con.get_server_info())

    cur = con.cursor()

except Error as error:
    print("Database connection error: ", error)

else:
    class Student:
        def __init__(self, window):
            self.window = window
            self.window.title("Student Management System.")
            self.window.geometry("1920x10180")

            title = Label(self.window, text="Student Management System",
                          font=("cambria", 40, "bold"), bg="light blue", bd=5, relief=GROOVE)
            title.pack(side=TOP, fill=X)

        # ==============================All Variables==============================
            self.Roll_No_var = StringVar()
            self.Name_var = StringVar()
            self.Email_var = StringVar()
            self.Gender_var = StringVar()
            self.Contact_var = StringVar()
            self.DOB_var = StringVar()

            self.search_by_var = StringVar()
            self.txt_search_var = StringVar()

        # ==============================Manage Frame==============================
            manage_frame = Frame(self.window, bd=5, relief=RIDGE, bg="light blue")
            manage_frame.place(x=20, y=100, width=700, height=800)

            # ==============================Title Frame==============================
            title_frame = Frame(manage_frame, bg="light blue")
            title_frame.place(x=5, y=3, width=680, height=60)

            m_title = Label(title_frame, text="Manage Student's Details", bg='blue', font=("cambria", 20, "bold"))
            m_title.grid(row=0, column=0, pady=20)

            # ==============================Detail Frame==============================
            detail_frame = Frame(manage_frame, bg="light blue")
            detail_frame.place(x=5, y=70, width=680, height=500)

            lbl_roll = Label(detail_frame, text="Roll No.", bg="light blue", font=("cambria", 20, "bold"))
            lbl_roll.grid(row=1, column=0, padx=50, pady=10, sticky="w")

            ent_roll = Entry(detail_frame, textvariable=self.Roll_No_var, font=("cambria", 20, "bold"), bd=3, relief=SUNKEN)
            ent_roll.grid(row=1, column=1, padx=50, pady=10, sticky="w")

            lbl_name = Label(detail_frame, text="Name", bg="light blue", font=("cambria", 20, "bold"))
            lbl_name.grid(row=2, column=0, padx=50, pady=10, sticky="w")

            ent_name = Entry(detail_frame, textvariable=self.Name_var, font=("cambria", 20, "bold"), bd=3, relief=SUNKEN)
            ent_name.grid(row=2, column=1, padx=50, pady=10, sticky="w")

            lbl_email = Label(detail_frame, text="Email", bg="light blue", font=("cambria", 20, "bold"))
            lbl_email.grid(row=3, column=0, padx=50, pady=10, sticky="w")

            ent_email = Entry(detail_frame, textvariable=self.Email_var, font=("cambria", 20, "bold"), bd=3, relief=SUNKEN)
            ent_email.grid(row=3, column=1, padx=50, pady=10, sticky="w")

            lbl_gender = Label(detail_frame, text="Gender", bg="light blue", font=("cambria", 20, "bold"))
            lbl_gender.grid(row=4, column=0, padx=50, pady=10, sticky="w")

            combo_gender = ttk.Combobox(detail_frame, textvariable=self.Gender_var,width=20, font=("cambria", 19, "bold"),
                                        state="readonly")
            combo_gender["values"] = ("Male", "Female", "Other")
            combo_gender.grid(row=4, column=1, padx=50, pady=10, sticky="w")

            lbl_contact = Label(detail_frame, text="Contact", bg="light blue", font=("cambria", 20, "bold"))
            lbl_contact.grid(row=5, column=0, padx=50, pady=10, sticky="w")

            ent_contact = Entry(detail_frame, textvariable=self.Contact_var, font=("cambria", 20, "bold"), bd=3, relief=SUNKEN)
            ent_contact.grid(row=5, column=1, padx=50, pady=10, sticky="w")

            lbl_dob = Label(detail_frame, text="D.O.B", bg="light blue", font=("cambria", 20, "bold"))
            lbl_dob.grid(row=6, column=0, padx=50, pady=10, sticky="w")

            ent_dob = Entry(detail_frame, textvariable=self.DOB_var, font=("cambria", 20, "bold"), bd=3, relief=SUNKEN)
            ent_dob.grid(row=6, column=1, padx=50, pady=10, sticky="w")

            lbl_address = Label(detail_frame, text="Address", bg="light blue", font=("cambria", 20, "bold"))
            lbl_address.grid(row=7, column=0, padx=50, pady=10, sticky="w")

            self.txt_address = Text(detail_frame, width=40, height=4)
            self.txt_address.grid(row=7, column=1, padx=50, pady=10, sticky="w")

            # ==============================Button Frame==============================
            button_frame = Frame(manage_frame, bg="green", bd=4, relief=SUNKEN)
            button_frame.place(x=40, y=520, width=600, height=100)

            btn_add = Button(button_frame, text="Add", font=("cambria", 20, "normal"),
                             bg="orange", bd=4, relief=GROOVE, command=self.add)
            btn_add.pack(side=LEFT, padx=25)

            btn_update = Button(button_frame, text="Update", font=("cambria", 20, "normal"),
                                bg="orange", bd=4, relief=GROOVE, command=self.update)
            btn_update.pack(side=LEFT, padx=25)

            btn_delete = Button(button_frame, text="Delete", font=("cambria", 20, "normal"),
                                bg="orange", bd=4, relief=GROOVE, command=self.delete)
            btn_delete.pack(side=LEFT, padx=25)

            btn_clear = Button(button_frame, text="Clear", font=("cambria", 20, "normal"),
                               bg="orange", bd=4, relief=GROOVE, command=self.clear)
            btn_clear.pack(side=LEFT, padx=25)

        # ==============================Search Frame==============================
            search_frame = Frame(self.window, bd=5, relief=RIDGE, bg="light blue")
            search_frame.place(x=800, y=100, width=1000, height=800)

            lbl_search = Label(search_frame, text="Search By", bg="light blue", font=("cambria", 20, "bold"))
            lbl_search.grid(row=0, column=0, padx=5, pady=10, sticky="w")

            combo_search = ttk.Combobox(search_frame, textvariable=self.search_by_var, width=10,
                                        font=("cambria", 19, "bold"), state="readonly")
            combo_search["values"] = ("Roll_NO", "Name", "Contact")
            combo_search.grid(row=0, column=1, padx=5, pady=10, sticky="w")

            txt_search = Entry(search_frame, textvariable=self.txt_search_var, width=15, font=("cambria", 20, "bold"),
                               bd=3, relief=SUNKEN)
            txt_search.grid(row=0, column=2, padx=5, pady=10, sticky="w")

            btn_search = Button(search_frame, text="Search", font=("cambria", 15, "normal"), bd=4, relief=GROOVE,
                                command=self.search_data)
            btn_search.grid(row=0, column=4, padx=5, pady=10, sticky="w")

            btn_show_all = Button(search_frame, text="Show All", font=("cambria", 15, "normal"), bd=4, relief=GROOVE,
                                  command=self.fetch_data)
            btn_show_all.grid(row=0, column=5, padx=5, pady=10, sticky="w")

            # ==============================table Frame==============================
            table_frame = Frame(search_frame, bd=5, relief=RIDGE)
            table_frame.place(x=20, y=70, width=950, height=700)

            table_scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
            table_scroll_x.pack(side=BOTTOM, fill=X)
            table_scroll_y = Scrollbar(table_frame, orient=VERTICAL)
            table_scroll_y.pack(side=RIGHT, fill=Y)
            self.table_student = ttk.Treeview(table_frame, columns=("1", "2", "3", "4", "5", "6", "7"),
                                         xscrollcommand=table_scroll_x.set, yscrollcommand=table_scroll_y.set)
            self.table_student.bind("<ButtonRelease-1>", self.get_data)
            table_scroll_x.config(command=self.table_student.xview)
            table_scroll_y.config(command=self.table_student.yview)

            self.table_student.heading("1", text="Roll No.")
            self.table_student.heading("2", text="Name")
            self.table_student.heading("3", text="Email")
            self.table_student.heading("4", text="Gender")
            self.table_student.heading("5", text="Contact")
            self.table_student.heading("6", text="D.O.B")
            self.table_student.heading("7", text="Address")
            self.table_student['show'] = "headings"

            self.table_student.column("1", width=100)
            self.table_student.column("2", width=350)
            self.table_student.column("3", width=300)
            self.table_student.column("4", width=100)
            self.table_student.column("5", width=150)
            self.table_student.column("6", width=150)
            self.table_student.column("7", width=500)

            self.table_student.pack(fill=BOTH, expand=1)
            self.fetch_data()

        # ==============================Functions==============================
        def add(self):
            if self.Roll_No_var.get() == "" or self.Name_var.get() == "" or self.Email_var.get() == "" \
                    or self.Gender_var.get() == "" or self.Contact_var.get() == "" or self.DOB_var.get() == "" \
                    or self.txt_address.get("1.0", END) == "":
                messagebox.showerror("Unfulfilled Boxes", "Please fill all the boxes first!")
            else:
                query = "insert into students values(%s, %s, %s, %s, %s, %s, %s);"
                values = (int(self.Roll_No_var.get()), self.Name_var.get(), self.Email_var.get(), self.Gender_var.get(),
                          self.Contact_var.get(), self.DOB_var.get(), self.txt_address.get("1.0", END))
                cur.execute(query, values)
                con.commit()
                self.fetch_data()
                messagebox.showinfo("Data Added Successful", "You have successfully added One data.")

        def fetch_data(self):
            query = "select * from students;"
            cur.execute(query)
            records = cur.fetchall()
            if len(records) != 0:
                self.table_student.delete(*self.table_student.get_children())
                for i in records:
                    self.table_student.insert("", END, values=i)

        def get_data(self, p):
            cursor_row = self.table_student.focus()
            contents = self.table_student.item(cursor_row)
            row = contents["values"]

            self.Roll_No_var.set(row[0])
            self.Name_var.set(row[1])
            self.Email_var.set(row[2])
            self.Gender_var.set(row[3])
            self.Contact_var.set(row[4])
            self.DOB_var.set(row[5])
            self.txt_address.delete("1.0", END)
            self.txt_address.insert(END, row[6])

        def update(self):
            query = "select * from students;"
            cur.execute(query)
            records = cur.fetchall()
            id_list = []
            for i in records:
                id_list.append(i[0])

            if self.Roll_No_var.get() == "":
                messagebox.showerror("Unfulfilled Roll No.", "you must enter the Roll NO. to update!")
            elif int(self.Roll_No_var.get()) not in id_list:
                messagebox.showerror("Unknown Roll NO.", "No such ID in database!")
            else:
                query = "Update students set Name=%s, Email=%s, Gender=%s, Contact=%s, " \
                        "DOB=%s, Address=%s where Roll_NO=%s;"
                values = (self.Name_var.get(), self.Email_var.get(), self.Gender_var.get(),
                          self.Contact_var.get(), self.DOB_var.get(),
                          self.txt_address.get("1.0", END), int(self.Roll_No_var.get()))
                cur.execute(query, values)
                con.commit()
                messagebox.showinfo("Data Updated Successful", "You have successfully updated One data.")



        def delete(self):
            query = "select * from students;"
            cur.execute(query)
            records = cur.fetchall()
            id_list = []
            for i in records:
                id_list.append(i[0])

            if self.Roll_No_var.get() == "":
                messagebox.showerror("Unfulfilled Roll No.", "you must enter the Roll NO. to delete!")
            elif int(self.Roll_No_var.get()) not in id_list:
                messagebox.showerror("Unknown Roll NO.", "No such ID in database!")
            else:
                query = "delete from students where Roll_NO=%s"
                values = (int(self.Roll_No_var.get()),)
                cur.execute(query, values)
                con.commit()
                messagebox.showinfo("Data Deleted Successful", "You have successfully deleted One data.")


        def clear(self):
            self.Roll_No_var.set("")
            self.Name_var.set("")
            self.Email_var.set("")
            self.Gender_var.set("")
            self.Contact_var.set("")
            self.DOB_var.set("")
            self.txt_address.delete("1.0", END)

        def search_data(self):
            if self.search_by_var.get() == "" or self.txt_search_var.get() == "":
                messagebox.showerror("Unfulfilled Boxes", "you must fill the boxes completely!")
            else:
                query_1= "select * from students where Roll_NO = %s;"
                query_2 = "select * from students where Name = %s;"
                query_3 = "select * from students where Contact = %s;"
                values = (self.txt_search_var.get(),)
                if self.search_by_var.get() == "Roll_NO":
                    cur.execute(query_1, values)
                elif self.search_by_var.get() == "Name":
                    cur.execute(query_2, values)
                else:
                    cur.execute(query_3, values)
                records = cur.fetchall()
                if len(records) != 0:
                    self.table_student.delete(*self.table_student.get_children())
                    for i in records:
                        self.table_student.insert("", END, values=i)



    window = Tk()
    Student(window)
    window.mainloop()

finally:
    if cur:
        cur.close()

    if con:
        con.close()