from tkinter import *
from tkinter import messagebox

from Model.Student import *
from Back_End.Connection import *


class MainInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("This is sample.")
        self.root.geometry("400x500")

        # ==========================Heading==========================
        self.db_connect = DbConnection()

        # ==========================Heading==========================
        heading = Label(self.root, text="My Sample Application", bg="yellow", font=("arial", 20, 'bold'))
        heading.pack(side=TOP, fill=X)

        # ==========================Frame in Window==========================
        main_frame = Frame(self.root, bg="light blue")
        main_frame.place(x=30, y=50, width=330, height=300)

        btn_frame = Frame(self.root, bg="light green", bd=5)
        btn_frame.place(x=30, y=350, width=330, height=60)

        # ==========================Widget in main frame==========================
        lbl_id = Label(main_frame, text="ID", font=('arial', 15, "bold"))
        lbl_id.grid(row=0, column=0, padx=10, pady=10)

        self.ent_id = Entry(main_frame)
        self.ent_id.grid(row=0, column=1)

        lbl_name = Label(main_frame, text="Name", font=('arial', 15, "bold"))
        lbl_name.grid(row=1, column=0, padx=10, pady=10)

        self.ent_name = Entry(main_frame)
        self.ent_name.grid(row=1, column=1)

        # ==========================Widget in main frame==========================
        btn_add = Button(btn_frame, text="Add", font=('arial', 10, "bold"))
        btn_add.pack(side=LEFT, padx=10, pady=10)

        btn_clear = Button(btn_frame, text="Clear", font=('arial', 10, "bold"))
        btn_clear.pack(side=LEFT, padx=10, pady=10)

        btn_update = Button(btn_frame, text="Update", font=('arial', 10, "bold"))
        btn_update.pack(side=LEFT, padx=10, pady=10)

        btn_delete = Button(btn_frame, text="Delete", font=('arial', 10, "bold"))
        btn_delete.pack(side=LEFT, padx=10, pady=10)

    def add(self):
        stu_ref = Student(self.ent_id.get(), self.ent_name.get())
        query = "insert into student values(%s, %s)"
        values = (int(stu_ref.get_id()), stu_ref.get_name())
        self.db_connect.add(query, values)
        messagebox.showinfo("Success", "Data successfully added.")


Window = Tk()
MainInterface(Window)
Window.mainloop()