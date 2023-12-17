from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from PIL import ImageTk, Image

from Assignment_Model.Get_Set_Methods import *
from Assignment_Back_End.Connector import *


class LoginInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Management System")
        self.root.geometry("1920x1080")

        self.img1 = ImageTk.PhotoImage(Image.open("Image/a2.jpg"))
        self.image_label = Label(self.root, image=self.img1)
        self.image_label.place(y=70)

    # =======================================Heading=======================================
        head_label = Label(self.root, text="Book Management System",
                           font=("cambria", 40, "bold"), bg="light blue", bd=5, relief=GROOVE)
        head_label.pack(side=TOP, fill=X)

    # =======================================Login Frame=======================================
        lgn_frame = Frame(self.root, bg="light blue", bd=5, relief=RIDGE)
        lgn_frame.place(x=560, y=300, width=800, height=350)

        # =======================================Login Frame Labels=======================================
        lgn_label = Label(lgn_frame, text="Please! Login First With Your Account", font=("cambria", 20, "bold"),
                          bg="light blue")
        lgn_label.place(x=180, y=20)

        email_lbl = Label(lgn_frame, text="Email:", font=("cambria", 15, "normal"), bg="light blue")
        email_lbl.place(x=180, y=70)

        password_lbl = Label(lgn_frame, text="Password:", font=("cambria", 15, "normal"), bg="light blue")
        password_lbl.place(x=180, y=120)

        # =======================================Login Frame Entries=======================================
        self.email_ent = Entry(lgn_frame, font=("cambria", 15, "normal"), width=30, bd=3, relief=SUNKEN)
        self.email_ent.place(x=300, y=70)

        self.password_ent = Entry(lgn_frame, font=("cambria", 15, "normal"), show="*", width=30, bd=3, relief=SUNKEN)
        self.password_ent.place(x=300, y=120)

        # =======================================Login Frame Button=======================================
        lgn_btn = Button(lgn_frame, text="Login", font=("cambria", 15, "normal"), bg="green", fg="white",
                         command=self.login)
        lgn_btn.place(x=200, y=180, width=100, height=50)

        clear_btn = Button(lgn_frame, text="clear", font=("cambria", 15, "normal"), bg="light blue",
                           command=self.clear)
        clear_btn.place(x=350, y=180, width=100, height=50)

        exit_btn = Button(lgn_frame, text="Exit", font=("cambria", 15, "normal"), bg="dark red", fg="white",
                          command=root.destroy)
        exit_btn.place(x=500, y=180, width=100, height=50)

    # =======================================Method To Clear Entries=======================================
    def clear(self):
        self.email_ent.delete(0, END)
        self.password_ent.delete(0, END)

    # =======================================Method To Check Entries=======================================
    def login(self):
        # =======================================Email Validation=======================================
        import re
        regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"

        lgn_ref = Login(self.email_ent.get(), self.password_ent.get())
        if lgn_ref.get_email() == "" or lgn_ref.get_password() == "":
            messagebox.showerror("Unfulfilled Boxes", "Fill up all the boxes first!")

        elif not (re.search(regex, lgn_ref.get_email())):
            messagebox.showerror("Invalid Email", "Please put a valid email.")

        elif lgn_ref.get_email() == "gaurisharma358@gmail.com" and lgn_ref.get_password() == "bookstore@358":
            messagebox.showinfo("Login Successful", "You are successfully logged in.")
            btn_int = Toplevel()
            ButtonsInterface(btn_int)
            self.root.withdraw()
        else:
            messagebox.showerror("Wrong Email and Password", "Please! check your email and password again.")


class ButtonsInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Management System")
        self.root.geometry("1920x1080")

        self.img1 = ImageTk.PhotoImage(Image.open("Image/a4.jpg"))
        self.image_label = Label(self.root, image=self.img1)
        self.image_label.place(y=80)

    # =======================================Heading=======================================
        head_label = Label(self.root, text="Book Management System",
                           font=("cambria", 40, "bold"), bg="light blue", bd=5, relief=GROOVE)
        head_label.pack(side=TOP, fill=X)

    # =======================================Buttons=======================================
        book_btn = Button(self.root, text="Show Book Details", font=("harrington", 15, "normal"), bg="light blue",
                          command=lambda: self.new_window(BookInterface))
        book_btn.place(x=810, y=100, width=300, height=50)

        author_book_genre_btn = Button(self.root, text="Show Author and Book Genre Details",
                                       font=("harrington", 15, "normal"), bg="light blue",
                                       command=lambda: self.new_window(AuthorBookGenreInterface))
        author_book_genre_btn.place(x=760, y=250, width=400, height=50)

        book_manage_btn = Button(self.root, text="Add Books", font=("harrington", 15, "normal"), bg="light blue",
                                 command=lambda: self.new_window(AddBookInterface))
        book_manage_btn.place(x=810, y=400, width=300, height=50)

        author_book_genre_manage_btn = Button(self.root, text="Add Authors And Book Genres",
                                              font=("harrington", 15, "normal"), bg="light blue",
                                              command=lambda: self.new_window(AddAuthorBookGenreInterface))
        author_book_genre_manage_btn.place(x=760, y=550, width=400, height=50)

        lgn_out_btn = Button(self.root, text="Logout", font=("cambria", 15, "normal"), bg="blue",
                             command=self.old_window)
        lgn_out_btn.place(x=885, y=700, width=150, height=50)

    # =======================================Method To Open New Window=======================================
    def new_window(self, window_name):
        window = Toplevel()
        window_name(window)
        return self.root.withdraw()

    # =======================================Method To Open New Window=======================================
    def old_window(self):
        LoginInterface(Toplevel())
        self.root.withdraw()


class BookInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Management System")
        self.root.geometry("1920x1080")

    # =======================================Data List=======================================
        language = ("Nepali", "English", "Hindi", "Spanish", "French", "Russian", "Japanese", "Korean", "Chinese",
                    "German", "Urdu")
        author_query = "select Author_ID from authors;"
        author_data = DbConnection().select(author_query)
        book_genre_query = "select Book_Genre_ID from book_genres;"
        book_genre_data = DbConnection().select(book_genre_query)

    # =======================================Heading=======================================
        heading_label = Label(self.root, text="Book Management System",
                              font=("cambria", 40, "bold"), bg="light blue", bd=5, relief=GROOVE)
        heading_label.pack(side=TOP, fill=X)

    # =======================================Frames=======================================
        dtl_frame = Frame(self.root, bg="light blue", bd=5, relief=RIDGE)
        dtl_frame.place(x=10, y=100, width=1900, height=940)

        # =======================================Frame's Label=======================================
        search_lbl = Label(dtl_frame, text="Search", bg="light blue", font=("cambria", 25, "bold"))
        search_lbl.pack(side=TOP, pady=10, fill=X)

        search_by_lbl = Label(dtl_frame, text="Search By:", bg="light blue", font=("cambria", 25, "normal"))
        search_by_lbl.place(x=320, y=55)

        book_detail_lbl = Label(dtl_frame, text="Book Details", bg="light blue", font=("cambria", 25, "bold"))
        book_detail_lbl.place(x=1100, y=125)

        manage_book_detail_lbl = Label(dtl_frame, text="Manage Book Details",
                                       font=("cambria", 25, "bold"), bg="light blue")
        manage_book_detail_lbl.place(x=90, y=125)

        # =======================================Frame's Combobox And Entry=======================================
        self.search_combo = ttk.Combobox(dtl_frame, width=15, font=("cambria", 20, "normal"))
        self.search_combo["values"] = ("ISBN", "Book_Title", "Language", "Author_ID", "Book_Genre_ID",
                                       "Publication_Year")
        self.search_combo.place(x=500, y=60)

        self.search_ent = Entry(dtl_frame, font=("cambria", 20, "normal"),
                                width=20, bd=3, relief=SUNKEN)
        self.search_ent.place(x=780, y=60)

        # =======================================Frame's Buttons=======================================
        search_btn = Button(dtl_frame, text="Search", font=("cambria", 15, "normal"), width=15, bg="orange",
                            command=self.search_data)
        search_btn.place(x=1120, y=60)

        search_all_btn = Button(dtl_frame, text="Search All", font=("cambria", 15, "normal"), width=15, bg="orange",
                                command=self.fetch_data)
        search_all_btn.place(x=1305, y=60)

        clear_btn = Button(dtl_frame, text="Clear", font=("cambria", 15, "normal"), width=10, bg="light blue",
                           command=self.clear1)
        clear_btn.place(x=1490, y=60)

        back_btn = Button(dtl_frame, text="Back", font=("cambria", 15, "normal"), width=15, bg="blue",
                          command=self.old_window)
        back_btn.place(x=860, y=880)

        # =======================================Frame's update and delete Frame=======================================
        update_delete_frame = Frame(dtl_frame, bg="light blue", bd=5, relief=SUNKEN)
        update_delete_frame.place(x=10, y=170, width=490, height=700)

        # ================================Frame's update and delete Frame Labels================================
        isbn_lbl = Label(update_delete_frame, text="ISBN:", bg="light blue", font=("cambria", 15, "normal"))
        isbn_lbl.place(x=20, y=50)

        book_title_lbl = Label(update_delete_frame, text="Book Title:", bg="light blue", font=("cambria", 15, "normal"))
        book_title_lbl.place(x=20, y=160)

        language_lbl = Label(update_delete_frame, text="Language:", bg="light blue", font=("cambria", 15, "normal"))
        language_lbl.place(x=20, y=230)

        author_id_lbl = Label(update_delete_frame, text="Author ID:", bg="light blue", font=("cambria", 15, "normal"))
        author_id_lbl.place(x=20, y=300)

        book_genre_id_lbl = Label(update_delete_frame, text="Book Genre ID:", bg="light blue",
                                  font=("cambria", 15, "normal"))
        book_genre_id_lbl.place(x=20, y=370)

        publication_year_lbl = Label(update_delete_frame, text="Publication Year:", bg="light blue",
                                     font=("cambria", 15, "normal"))
        publication_year_lbl.place(x=20, y=440)

        price_lbl = Label(update_delete_frame, text="Price:", bg="light blue", font=("cambria", 15, "normal"))
        price_lbl.place(x=20, y=510)

        no_of_copies_lbl = Label(update_delete_frame, text="No Of Copies:", bg="light blue",
                                 font=("cambria", 15, "normal"))
        no_of_copies_lbl.place(x=20, y=580)

        # ================================Frame's update and delete Frame Entries================================
        self.isbn_ent = Entry(update_delete_frame, font=("cambria", 15, "normal"), width=25, bd=3, relief=SUNKEN)
        self.isbn_ent.place(x=180, y=50)

        self.book_title_ent = Entry(update_delete_frame, font=("cambria", 15, "normal"), width=25, bd=3, relief=SUNKEN)
        self.book_title_ent.place(x=180, y=160)

        self.language_combo = ttk.Combobox(update_delete_frame, font=("cambria", 15, "normal"), width=24)
        self.language_combo["values"] = language
        self.language_combo.place(x=180, y=230)

        self.author_id_combo = ttk.Combobox(update_delete_frame, font=("cambria", 15, "normal"), width=24)
        self.author_id_combo["values"] = author_data
        self.author_id_combo.place(x=180, y=300)

        self.book_genre_id_combo = ttk.Combobox(update_delete_frame, font=("cambria", 15, "normal"), width=24)
        self.book_genre_id_combo["values"] = book_genre_data
        self.book_genre_id_combo.place(x=180, y=370)

        self.publication_year_ent = Entry(update_delete_frame, font=("cambria", 15, "normal"), width=25, bd=3,
                                          relief=SUNKEN)
        self.publication_year_ent.place(x=180, y=440)

        self.price_ent = Entry(update_delete_frame, font=("cambria", 15, "normal"), width=25, bd=3, relief=SUNKEN)
        self.price_ent.place(x=180, y=510)

        self.no_of_copies_ent = Entry(update_delete_frame, font=("cambria", 15, "normal"), width=25, bd=3,
                                      relief=SUNKEN)
        self.no_of_copies_ent.place(x=180, y=580)

        # ================================Frame's update and delete Frame Buttons================================
        update_btn = Button(update_delete_frame, text="Update", font=("cambria", 15, "normal"), bg="dark orange",
                            width=8, command=self.update)
        update_btn.place(x=120, y=630)

        delete_btn = Button(update_delete_frame, text="Delete", font=("cambria", 15, "normal"), bg="red", width=8,
                            command=self.delete)
        delete_btn.place(x=360, y=100)

        clear_btn = Button(update_delete_frame, text="clear", font=("cambria", 15, "normal"), bg="light blue",
                           width=8, command=self.clear)
        clear_btn.place(x=270, y=630)

        # =======================================Frame's Scrollbar Frame=======================================
        scrollbar_frame = Frame(dtl_frame, bg="orange", bd=5, relief=SUNKEN)
        scrollbar_frame.place(x=510, y=170, width=1370, height=700)

        table_scroll_x = Scrollbar(scrollbar_frame, orient=HORIZONTAL)
        table_scroll_x.pack(side=BOTTOM, fill=X)
        table_scroll_y = Scrollbar(scrollbar_frame, orient=VERTICAL)
        table_scroll_y.pack(side=RIGHT, fill=Y)
        self.book_table = ttk.Treeview(scrollbar_frame, columns=("1", "2", "3", "4", "5", "6", "7", "8"),
                                       xscrollcommand=table_scroll_x.set, yscrollcommand=table_scroll_y.set)
        self.book_table.bind("<Double-1>", self.get_data)
        table_scroll_x.config(command=self.book_table.xview)
        table_scroll_y.config(command=self.book_table.yview)

        self.book_table.heading("1", text="ISBN")
        self.book_table.heading("2", text="Book_Title")
        self.book_table.heading("3", text="Language")
        self.book_table.heading("4", text="Author_ID")
        self.book_table.heading("5", text="Book_Genre_ID")
        self.book_table.heading("6", text="Publication_Year")
        self.book_table.heading("7", text="Price")
        self.book_table.heading("8", text="No_Of_Copies")
        self.book_table["show"] = "headings"

        self.book_table.column("1", width=250)
        self.book_table.column("2", width=400)
        self.book_table.column("3", width=250)
        self.book_table.column("4", width=200)
        self.book_table.column("5", width=200)
        self.book_table.column("6", width=250)
        self.book_table.column("7", width=250)
        self.book_table.column("8", width=200)

        self.book_table.pack(fill=BOTH, expand=1)
        self.fetch_data()

    # =======================================Method To Fetch Data======================================
    def fetch_data(self):
        query = "select * from books;"
        data = DbConnection().select(query)
        if len(data) != 0:
            self.book_table.delete(*self.book_table.get_children())
            for rows in data:
                self.book_table.insert("", END, values=rows)
        else:
            self.book_table.delete(*self.book_table.get_children())

    # =======================================Method To Get Data======================================
    def get_data(self, get):
        cursor_row = self.book_table.focus()
        data = self.book_table.item(cursor_row)
        row = data["values"]

        self.isbn_ent.delete(0, END)
        self.book_title_ent.delete(0, END)
        self.language_combo.delete(0, END)
        self.author_id_combo.delete(0, END)
        self.book_genre_id_combo.delete(0, END)
        self.publication_year_ent.delete(0, END)
        self.price_ent.delete(0, END)
        self.no_of_copies_ent.delete(0, END)

        self.isbn_ent.insert(0, row[0])
        self.book_title_ent.insert(0, row[1])
        self.language_combo.insert(0, row[2])
        self.author_id_combo.insert(0, row[3])
        self.book_genre_id_combo.insert(0, row[4])
        self.publication_year_ent.insert(0, row[5])
        self.price_ent.insert(0, row[6][3:])
        self.no_of_copies_ent.insert(0, row[7])

    # =======================================Method To Fetch Data======================================
    def search_data(self):
        if self.search_combo.get() == "" or self.search_ent.get() == "":
            messagebox.showerror("Unfulfilled Boxes", "Please fill all the boxes first!")
        else:
            query1 = "select * from books where ISBN=%s;"
            query2 = "select * from books where Book_Title=%s;"
            query3 = "select * from books where Language=%s;"
            query4 = "select * from books where Author_ID=%s;"
            query5 = "select * from books where Book_Genre_ID=%s;"
            query6 = "select * from books where Publication_Year=%s;"
            values = (self.search_ent.get(),)
            data = None

            if self.search_combo.get() == "ISBN":
                data = DbConnection().search(query1, values)
            elif self.search_combo.get() == "Book_Title":
                data = DbConnection().search(query2, values)
            elif self.search_combo.get() == "Language":
                data = DbConnection().search(query3, values)
            elif self.search_combo.get() == "Author_ID":
                data = DbConnection().search(query4, values)
            elif self.search_combo.get() == "Book_Genre_ID":
                data = DbConnection().search(query5, values)
            else:
                data = DbConnection().search(query6, values)

            if len(data) != 0:
                self.book_table.delete(*self.book_table.get_children())
                for rows in data:
                    self.book_table.insert("", END, values=rows)

    # =======================================Method To search data linearly=======================================
    @classmethod
    def linear_search(cls, a_list, search_item):
        for i in range(len(a_list)):
            if search_item == a_list[i]:
                return True
        return False

    # =======================================Method To update Data======================================
    def update(self):
        query = "select * from books;"
        data = DbConnection().select(query)
        isbn = []
        if len(data) != 0:
            for row in data:
                isbn.append(row[0])
        a = True
        try:
            if self.isbn_ent.get() == "" or self.book_title_ent.get() == "" or self.language_combo.get() == "" or \
                    self.author_id_combo.get() == "" or self.book_genre_id_combo.get() == "" or \
                    self.publication_year_ent.get() == "" or self.price_ent.get() == "" or \
                    self.no_of_copies_ent.get() == "":
                messagebox.showerror("Unfulfilled Boxes", "Please fill all the boxes first!")
            else:
                try:
                    a = int(self.book_title_ent.get())
                    messagebox.showerror("Invalid Input", "Please! Enter letters in 'Book Title'.")
                except ValueError:
                    b = int(self.language_combo.get())
                    messagebox.showerror("Invalid Input", "Please! Enter letters in 'Language'.")
        except ValueError:
            try:
                if int(self.isbn_ent.get()) == int or int(self.author_id_combo.get()) == int or \
                       int(self.book_genre_id_combo.get()) == int or int(self.publication_year_ent.get()) == int or \
                       int(self.price_ent.get()) == int or int(self.no_of_copies_ent.get()) == int:
                    a = True
            except ValueError:
                messagebox.showerror("Invalid Input", "Please! Enter number in ISBN, Author ID, Book Genre ID,"
                                     " Publication Year and No Of Copies.")
            else:
                if self.linear_search(isbn, self.isbn_ent.get()) == a:  # Linear Searching
                    book = BookADDUpdate(self.isbn_ent.get(), self.book_title_ent.get(), self.language_combo.get(),
                                         self.author_id_combo.get(), self.book_genre_id_combo.get(),
                                         self.publication_year_ent.get(), self.price_ent.get(),
                                         self.no_of_copies_ent.get())
                    query = "update books set Book_Title=%s, Language=%s, Author_ID=%s, Book_Genre_ID=%s, " \
                            "Publication_Year=%s, Price=%s, No_Of_Copies=%s where ISBN=%s;"
                    values = (book.get_book_title(), book.get_language(), int(book.get_author_id()),
                              int(book.get_book_genre_id()), book.get_publication_year(), "Rs." + book.get_price(),
                              book.get_no_of_copies(), book.get_isbn())
                    DbConnection().update(query, values)
                    DbConnection().close()
                    messagebox.showinfo("Data update complete", "One book is successfully updated.")
                    self.fetch_data()
                else:
                    messagebox.showerror("Unmatched ISBN", "Please enter correct ISBN.")

    # =======================================Method To delete Data======================================
    def delete(self):
        query = "select * from books;"
        data = DbConnection().select(query)
        isbn = []
        if len(data) != 0:
            for row in data:
                isbn.append(row[0])
        a = True
        if self.isbn_ent.get() == "":
            messagebox.showerror("Unfulfilled Box", "Please fill ISBN box first!")
        else:
            if self.linear_search(isbn, self.isbn_ent.get()) == a:  # Linear Searching
                book = BookDelete(self.isbn_ent.get())
                query = "delete from books where ISBN=%s;"
                values = (book.get_isbn(),)
                DbConnection().delete(query, values)
                DbConnection().close()
                messagebox.showinfo("Data delete complete", "One book is successfully deleted.")
                self.fetch_data()
            else:
                messagebox.showerror("Unmatched ISBN", "Please enter correct ISBN.")

    # =======================================Method To clear Combo and Entries=======================================
    def clear1(self):
        self.search_combo.delete(0, END)
        self.search_ent.delete(0, END)

    # =======================================Method To clear Entries=======================================
    def clear(self):
        self.isbn_ent.delete(0, END)
        self.book_title_ent.delete(0, END)
        self.language_combo.delete(0, END)
        self.author_id_combo.delete(0, END)
        self.book_genre_id_combo.delete(0, END)
        self.publication_year_ent.delete(0, END)
        self.price_ent.delete(0, END)
        self.no_of_copies_ent.delete(0, END)

    # =======================================Method To Open New Window=======================================
    def old_window(self):
        ButtonsInterface(Toplevel())
        self.root.withdraw()


class AuthorBookGenreInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Management System")
        self.root.geometry("1920x1080")

    # =======================================Heading=======================================
        head_label = Label(self.root, text="Book Management System",
                           font=("cambria", 40, "bold"), bg="light blue", bd=5, relief=GROOVE)
        head_label.pack(side=TOP, fill=X)

    # =======================================Frames=======================================
        dtl_frame = Frame(self.root, bg="light blue", bd=5, relief=RIDGE)
        dtl_frame.place(x=10, y=100, width=1900, height=940)

        # =======================================Frame's Label=======================================
        # =======================================Author=======================================
        author_search_lbl = Label(dtl_frame, text="Search Author", bg="light blue", font=("cambria", 20, "bold"))
        author_search_lbl.place(x=350, y=10)

        author_search_by_lbl = Label(dtl_frame, text="Search By:", bg="light blue", font=("cambria", 20, "normal"))
        author_search_by_lbl.place(x=10, y=55)

        author_detail_lbl = Label(dtl_frame, text="Author Details", bg="light blue", font=("cambria", 20, "bold"))
        author_detail_lbl.place(x=350, y=295)

        manage_author_detail_lbl = Label(dtl_frame, text="Manage Author Details",
                                         font=("cambria", 20, "bold"), bg="light blue")
        manage_author_detail_lbl.place(x=280, y=115)

        # =======================================Book Genre=======================================
        book_genre_search_lbl = Label(dtl_frame, text="Search Book Genre", bg="light blue",
                                      font=("cambria", 20, "bold"))
        book_genre_search_lbl.place(x=1300, y=10)

        book_genre_search_by_lbl = Label(dtl_frame, text="Search By:", bg="light blue", font=("cambria", 20, "normal"))
        book_genre_search_by_lbl.place(x=960, y=55)

        book_genre_detail_lbl = Label(dtl_frame, text="Book Genre Details", bg="light blue", font=("cambria", 20, "bold"))
        book_genre_detail_lbl.place(x=1300, y=295)

        manage_book_genre_detail_lbl = Label(dtl_frame, text="Manage Book Genre Details",
                                             font=("cambria", 20, "bold"), bg="light blue")
        manage_book_genre_detail_lbl.place(x=1230, y=115)

        bar_lbl = Label(dtl_frame, bg="dark green", bd=5, relief=GROOVE)
        bar_lbl.place(x=945, y=10, width=5, height=860)

        # =======================================Frame's Combobox And Entry=======================================
        # =======================================Author=======================================
        self.author_search_combo = ttk.Combobox(dtl_frame, width=10, font=("cambria", 20, "normal"))
        self.author_search_combo["values"] = ("Author_ID", "Author_First_Name", "Author_Last_Name")
        self.author_search_combo.place(x=150, y=60)

        self.author_search_ent = Entry(dtl_frame, font=("cambria", 20, "normal"), width=15, bd=3, relief=SUNKEN)
        self.author_search_ent.place(x=340, y=60)

        # =======================================Book Genre=======================================
        self.book_genre_search_combo = ttk.Combobox(dtl_frame, width=10, font=("cambria", 20, "normal"))
        self.book_genre_search_combo["values"] = ("Book_Genre_ID", "Book_Genre_Name")
        self.book_genre_search_combo.place(x=1100, y=60)

        self.book_genre_search_ent = Entry(dtl_frame, font=("cambria", 20, "normal"), width=15, bd=3, relief=SUNKEN)
        self.book_genre_search_ent.place(x=1290, y=60)

        # =======================================Frame's Buttons=======================================
        # =======================================Author=======================================
        author_search_btn = Button(dtl_frame, text="Search", font=("cambria", 15, "normal"), width=10, bg="orange",
                                   command=self.author_search_data)
        author_search_btn.place(x=600, y=60)

        author_search_all_btn = Button(dtl_frame, text="Search All", font=("cambria", 15, "normal"),
                                       width=10, bg="orange", command=self.author_fetch_data)
        author_search_all_btn.place(x=730, y=60)

        author_clear_btn = Button(dtl_frame, text="Clear", font=("cambria", 10, "normal"),
                                  width=10, bg="light blue", command=self.author_clear1)
        author_clear_btn.place(x=860, y=65)

        # =======================================Book Genre=======================================
        book_genre_search_btn = Button(dtl_frame, text="Search", font=("cambria", 15, "normal"), width=10, bg="orange",
                                       command=self.book_genre_search_data)
        book_genre_search_btn.place(x=1550, y=60)

        book_genre_search_all_btn = Button(dtl_frame, text="Search All", font=("cambria", 15, "normal"), width=10,
                                           bg="orange", command=self.book_genre_fetch_data)
        book_genre_search_all_btn.place(x=1680, y=60)

        book_genre_clear_btn = Button(dtl_frame, text="Clear", font=("cambria", 10, "normal"),
                                      width=10, bg="light blue", command=self.book_genre_clear1)
        book_genre_clear_btn.place(x=1810, y=65)

        back_btn = Button(dtl_frame, text="Back", font=("cambria", 15, "normal"), width=15, bg="blue",
                          command=self.old_window)
        back_btn.place(x=860, y=880)

        # =======================================Frame's update and delete Frame=======================================
        author_update_delete_frame = Frame(dtl_frame, bg="light blue", bd=5, relief=SUNKEN)
        author_update_delete_frame.place(x=10, y=160, width=920, height=120)

        book_genre_update_delete_frame = Frame(dtl_frame, bg="light blue", bd=5, relief=SUNKEN)
        book_genre_update_delete_frame.place(x=960, y=160, width=920, height=120)

        # ================================Frame's update and delete Frame Labels================================
        # =======================================Author=======================================
        author_id_lbl = Label(author_update_delete_frame, text="ID:", bg="light blue",
                              font=("cambria", 15, "normal"))
        author_id_lbl.place(x=10, y=10)

        author_first_name_lbl = Label(author_update_delete_frame, text="First Name:", bg="light blue",
                                      font=("cambria", 15, "normal"))
        author_first_name_lbl.place(x=135, y=10)

        author_last_name_lbl = Label(author_update_delete_frame, text="Last Name:", bg="light blue",
                                     font=("cambria", 15, "normal"))
        author_last_name_lbl.place(x=430, y=10)

        author_no_of_book_lbl = Label(author_update_delete_frame, text="No Of Books:", bg="light blue",
                                      font=("cambria", 15, "normal"))
        author_no_of_book_lbl.place(x=715, y=10)

        # =======================================Book Genre=======================================
        book_genre_id_lbl = Label(book_genre_update_delete_frame, text="ID:", bg="light blue",
                                  font=("cambria", 15, "normal"))
        book_genre_id_lbl.place(x=10, y=10)

        book_genre_name_lbl = Label(book_genre_update_delete_frame, text="Book Genre Name:", bg="light blue",
                                    font=("cambria", 15, "normal"))
        book_genre_name_lbl.place(x=240, y=10)

        book_genre_no_of_book_lbl = Label(book_genre_update_delete_frame, text="No Of Books:", bg="light blue",
                                          font=("cambria", 15, "normal"))
        book_genre_no_of_book_lbl.place(x=600, y=10)

        # ================================Frame's update and delete Frame Entries================================
        # =======================================Author=======================================
        self.author_id_ent = Entry(author_update_delete_frame,
                                   font=("cambria", 15, "normal"), width=7, bd=3, relief=SUNKEN)
        self.author_id_ent.place(x=40, y=10)

        self.author_first_name_ent = Entry(author_update_delete_frame,
                                           font=("cambria", 15, "normal"), width=15, bd=3, relief=SUNKEN)
        self.author_first_name_ent.place(x=245, y=10)

        self.author_last_name_ent = Entry(author_update_delete_frame,
                                          font=("cambria", 15, "normal"), width=15, bd=3, relief=SUNKEN)
        self.author_last_name_ent.place(x=535, y=10)

        self.author_no_of_book_ent = Entry(author_update_delete_frame,
                                           font=("cambria", 15, "normal"), width=5, bd=3, relief=SUNKEN)
        self.author_no_of_book_ent.place(x=835, y=10)

        # =======================================Book Genre=======================================
        self.book_genre_id_ent = Entry(book_genre_update_delete_frame,
                                       font=("cambria", 15, "normal"), width=15, bd=3, relief=SUNKEN)
        self.book_genre_id_ent.place(x=50, y=10)

        self.book_genre_name_combo = ttk.Combobox(book_genre_update_delete_frame, font=("cambria", 15, "normal"),
                                                  width=14)
        self.book_genre_name_combo["values"] = ('Action and Adventure', 'Art/Architecture', 'Biography',
                                                'Business/Economics', "Children's", 'Comic Book', 'Crime', 'Cultural',
                                                'Diary', 'Dictionary', 'Drama', 'Encyclopedia', 'Graphic novel',
                                                'Guide', 'Health', 'History', 'Horror', 'Humor', 'Journal', 'Math',
                                                'Mystery', 'Poetry', 'Review', 'Romance', 'Science', 'Science Fiction',
                                                'Sports', 'Story', 'Thriller', 'Travel')
        self.book_genre_name_combo.place(x=410, y=10)

        self.book_genre_no_of_book_ent = Entry(book_genre_update_delete_frame,
                                               font=("cambria", 15, "normal"), width=15, bd=3, relief=SUNKEN)
        self.book_genre_no_of_book_ent.place(x=720, y=10)

        # ================================Frame's update and delete Frame Buttons================================
        # =======================================Author=======================================
        author_update_btn = Button(author_update_delete_frame, text="Update", font=("cambria", 15, "normal"),
                                   bg="dark orange", width=8, command=self.author_update)
        author_update_btn.place(x=220, y=60)

        author_delete_btn = Button(author_update_delete_frame, text="Delete", font=("cambria", 15, "normal"),
                                   bg="red", width=8, command=self.author_delete)
        author_delete_btn.place(x=360, y=60)

        author_clear_btn = Button(author_update_delete_frame, text="clear", font=("cambria", 15, "normal"),
                                  bg="light blue", width=8, command=self.author_clear)
        author_clear_btn.place(x=500, y=60)

        # =======================================Book Genre=======================================
        book_genre_update_btn = Button(book_genre_update_delete_frame, text="Update", font=("cambria", 15, "normal"),
                                       bg="dark orange", width=8, command=self.book_genre_update)
        book_genre_update_btn.place(x=220, y=60)

        book_genre_delete_btn = Button(book_genre_update_delete_frame, text="Delete", font=("cambria", 15, "normal"),
                                       bg="red", width=8, command=self.book_genre_delete)
        book_genre_delete_btn.place(x=360, y=60)

        book_genre_clear_btn = Button(book_genre_update_delete_frame, text="clear", font=("cambria", 15, "normal"),
                                      bg="light blue", width=8, command=self.book_genre_clear)
        book_genre_clear_btn.place(x=500, y=60)

        # =======================================Frame's Scrollbar Frame=======================================
        # =======================================Author=======================================
        author_scrollbar_frame = Frame(dtl_frame, bg="orange", bd=5, relief=SUNKEN)
        author_scrollbar_frame.place(x=10, y=340, width=920, height=530)

        author_table_scroll_x = Scrollbar(author_scrollbar_frame, orient=HORIZONTAL)
        author_table_scroll_x.pack(side=BOTTOM, fill=X)
        author_table_scroll_y = Scrollbar(author_scrollbar_frame, orient=VERTICAL)
        author_table_scroll_y.pack(side=RIGHT, fill=Y)
        self.author_table = ttk.Treeview(author_scrollbar_frame, columns=("1", "2", "3", "4"),
                                         xscrollcommand=author_table_scroll_x.set,
                                         yscrollcommand=author_table_scroll_y.set)
        self.author_table.bind("<Double-1>", self.author_get_data)
        author_table_scroll_x.config(command=self.author_table.xview)
        author_table_scroll_y.config(command=self.author_table.yview)

        self.author_table.heading("1", text="Author_ID")
        self.author_table.heading("2", text="Author_First_Name")
        self.author_table.heading("3", text="Author_Last_Name")
        self.author_table.heading("4", text="No_Of_Books")
        self.author_table["show"] = "headings"

        self.author_table.column("1", width=250)
        self.author_table.column("2", width=400)
        self.author_table.column("3", width=250)
        self.author_table.column("4", width=200)

        self.author_table.pack(fill=BOTH, expand=1)
        self.author_fetch_data()

        # =======================================Book Genre=======================================
        book_genre_scrollbar_frame = Frame(dtl_frame, bg="orange", bd=5, relief=SUNKEN)
        book_genre_scrollbar_frame.place(x=960, y=340, width=920, height=530)

        book_genre_table_scroll_x = Scrollbar(book_genre_scrollbar_frame, orient=HORIZONTAL)
        book_genre_table_scroll_x.pack(side=BOTTOM, fill=X)
        book_genre_table_scroll_y = Scrollbar(book_genre_scrollbar_frame, orient=VERTICAL)
        book_genre_table_scroll_y.pack(side=RIGHT, fill=Y)
        self.book_genre_table = ttk.Treeview(book_genre_scrollbar_frame, columns=("1", "2", "3"),
                                             xscrollcommand=book_genre_table_scroll_x.set,
                                             yscrollcommand=book_genre_table_scroll_y.set)
        self.book_genre_table.bind("<Double-1>", self.book_genre_get_data)
        book_genre_table_scroll_x.config(command=self.book_genre_table.xview)
        book_genre_table_scroll_y.config(command=self.book_genre_table.yview)

        self.book_genre_table.heading("1", text="Book_Genre_ID")
        self.book_genre_table.heading("2", text="Book_Genre_Name")
        self.book_genre_table.heading("3", text="No_Of_Books")
        self.book_genre_table["show"] = "headings"

        self.book_genre_table.column("1", width=300)
        self.book_genre_table.column("2", width=450)
        self.book_genre_table.column("3", width=300)

        self.book_genre_table.pack(fill=BOTH, expand=1)
        self.book_genre_fetch_data()

    # =======================================Method To Fetch Data======================================
    def author_fetch_data(self):
        query = "select * from authors;"
        data = DbConnection().select(query)
        if len(data) != 0:
            self.author_table.delete(*self.author_table.get_children())
            for rows in data:
                self.author_table.insert("", END, values=rows)
        else:
            self.author_table.delete(*self.author_table.get_children())

    def book_genre_fetch_data(self):
        query = "select * from book_genres;"
        data = DbConnection().select(query)
        if len(data) != 0:
            self.book_genre_table.delete(*self.book_genre_table.get_children())
            for rows in data:
                self.book_genre_table.insert("", END, values=rows)
        else:
            self.book_genre_table.delete(*self.book_genre_table.get_children())

    # =======================================Method To Get Data======================================
    def author_get_data(self, get):
        cursor_row = self.author_table.focus()
        data = self.author_table.item(cursor_row)
        row = data["values"]

        self.author_id_ent.delete(0, END)
        self.author_first_name_ent.delete(0, END)
        self.author_last_name_ent.delete(0, END)
        self.author_no_of_book_ent.delete(0, END)

        self.author_id_ent.insert(0, row[0])
        self.author_first_name_ent.insert(0, row[1])
        self.author_last_name_ent.insert(0, row[2])
        self.author_no_of_book_ent.insert(0, row[3])

    def book_genre_get_data(self, get):
        cursor_row = self.book_genre_table.focus()
        data = self.book_genre_table.item(cursor_row)
        row = data["values"]

        self.book_genre_id_ent.delete(0, END)
        self.book_genre_name_combo.delete(0, END)
        self.book_genre_no_of_book_ent.delete(0, END)

        self.book_genre_id_ent.insert(0, row[0])
        self.book_genre_name_combo.insert(0, row[1])
        self.book_genre_no_of_book_ent.insert(0, row[2])

    # =======================================Method To Search Data======================================
    def author_search_data(self):
        if self.author_search_combo.get() == "" or self.author_search_ent.get() == "":
            messagebox.showerror("Unfulfilled Boxes", "Please fill all the boxes first!")
        else:
            query1 = "select * from authors where Author_ID=%s;"
            query2 = "select * from authors where Author_First_Name=%s;"
            query3 = "select * from authors where Author_Last_Name=%s;"
            values = (self.author_search_ent.get(),)
            data = None

            if self.author_search_combo.get() == "Author_ID":
                data = DbConnection().search(query1, values)
            elif self.author_search_combo.get() == "Author_First_Name":
                data = DbConnection().search(query2, values)
            else:
                data = DbConnection().search(query3, values)

            if len(data) != 0:
                self.author_table.delete(*self.author_table.get_children())
                for rows in data:
                    self.author_table.insert("", END, values=rows)

    def book_genre_search_data(self):
        if self.book_genre_search_combo.get() == "" or self.book_genre_search_ent.get() == "":
            messagebox.showerror("Unfulfilled Boxes", "Please fill all the boxes first!")
        else:
            query1 = "select * from book_genres where Book_Genre_ID=%s;"
            query2 = "select * from book_genres where Book_Genre_Name=%s;"
            values = (self.book_genre_search_ent.get(),)
            data = None

            if self.book_genre_search_combo.get() == "Book_Genre_ID":
                data = DbConnection().search(query1, values)
            else:
                data = DbConnection().search(query2, values)

            if len(data) != 0:
                self.book_genre_table.delete(*self.book_genre_table.get_children())
                for rows in data:
                    self.book_genre_table.insert("", END, values=rows)

    # =======================================Method To sort numbers of the list======================================
    @classmethod
    def bubble_sort(cls, a_list):
        swap = True
        while swap:
            swap = False
            for i in range(len(a_list) - 1):
                if a_list[i] > a_list[i + 1]:
                    a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                    swap = True
        return a_list

    # =======================================Method To update Data======================================
    def author_update(self):
        query = "select * from authors;"
        data = DbConnection().select(query)
        author_id = []
        if len(data) != 0:
            for row in data:
                author_id.append(row[0])
        try:
            if self.author_id_ent.get() == "" or self.author_first_name_ent.get() == "" or \
                    self.author_last_name_ent.get() == "" or self.author_no_of_book_ent.get() == "":
                messagebox.showerror("Unfulfilled Boxes", "Please fill all the boxes first!")
            else:
                try:
                    a = int(self.author_first_name_ent.get())
                    messagebox.showerror("Invalid Input", "Please! Enter letters in 'Author first name'.")
                except ValueError:
                    b = int(self.author_last_name_ent.get())
                    messagebox.showerror("Invalid Input", "Please! Enter letters in 'Author last name'.")
        except ValueError:
            try:
                if int(self.author_id_ent.get()) == int or int(self.author_no_of_book_ent.get()) == int:
                    a = True
            except ValueError:
                messagebox.showerror("Invalid Input",
                                     "Please! Enter number in Author ID and No of Books.")
            else:
                if int(self.author_id_ent.get()) not in author_id:
                    messagebox.showerror("Unmatched ID", "Please enter correct ID.")
                else:
                    author = AuthorAddUpdate(self.author_id_ent.get(), self.author_first_name_ent.get(),
                                             self.author_last_name_ent.get(), self.author_no_of_book_ent.get())
                    query = "update authors set Author_First_Name=%s, Author_Last_Name=%s, No_Of_Books=%s where" \
                            " Author_ID=%s;"
                    values = (author.get_author_first_name(), author.get_author_last_name(),
                              author.get_no_of_books(), author.get_author_id())
                    DbConnection().update(query, values)
                    DbConnection().close()
                    messagebox.showinfo("Data update complete", "One Author is successfully updated.")
                    self.author_fetch_data()

    def book_genre_update(self):
        query = "select * from book_genres;"
        data = DbConnection().select(query)
        book_genre_id = []
        if len(data) != 0:
            for row in data:
                book_genre_id.append(row[0])
        try:
            if self.book_genre_id_ent.get() == "" or self.book_genre_name_combo.get() == "" or \
                   self.book_genre_no_of_book_ent.get() == "":
                messagebox.showerror("Unfulfilled Boxes", "Please fill all the boxes first!")
            else:
                a = int(self.book_genre_name_combo.get())
                messagebox.showerror("Invalid Input", "Please! Enter letters in 'Book Genre name'.")
        except ValueError:
            try:
                if int(self.book_genre_id_ent.get()) == int or int(self.book_genre_no_of_book_ent.get()) == int:
                    a = True
            except ValueError:
                messagebox.showerror("Invalid Input",
                                     "Please! Enter number in Book Genre ID and No of Books.")
            else:
                if int(self.book_genre_id_ent.get()) not in book_genre_id:
                    messagebox.showerror("Unmatched ID", "Please enter correct ID.")
                else:
                    book_genre = BookGenreAddUpdate(self.book_genre_id_ent.get(), self.book_genre_name_combo.get(),
                                                    self.book_genre_no_of_book_ent.get())
                    query = "update book_genres set Book_Genre_Name=%s, No_Of_Books=%s where Book_Genre_ID=%s;"
                    values = (book_genre.get_book_genre_name(), book_genre.get_no_of_books(),
                              book_genre.get_book_genre_id())
                    DbConnection().update(query, values)
                    DbConnection().close()
                    messagebox.showinfo("Data update complete", "One Book Genre is successfully updated.")
                    self.book_genre_fetch_data()

    # =======================================Method To delete Data======================================
    def author_delete(self):
        query = "select * from authors;"
        data = DbConnection().select(query)
        author_id = []
        if len(data) != 0:
            for row in data:
                author_id.append(row[0])
        if self.author_id_ent.get() == "":
            messagebox.showerror("Unfulfilled Box", "Please fill ID box first!")
        else:
            try:
                if int(self.author_id_ent.get()) not in author_id:  # Searching
                    messagebox.showerror("Unmatched ID", "Please enter correct ID.")
                else:
                    author = AuthorDelete(self.author_id_ent.get())
                    query = "delete from authors where Author_ID=%s;"
                    values = (author.get_author_id(),)
                    DbConnection().delete(query, values)
                    DbConnection().close()
                    messagebox.showinfo("Data delete complete", "One author is successfully deleted.")
                    self.author_fetch_data()
            except ValueError:
                messagebox.showerror("Invalid Input ID", "Please enter number in ID.")

    def book_genre_delete(self):
        query = "select * from book_genres;"
        data = DbConnection().select(query)
        book_genre_id = []
        if len(data) != 0:
            for row in data:
                book_genre_id.append(row[0])
        if len(book_genre_id) >= 2:
            book_genre_id[0], book_genre_id[1] = book_genre_id[1], book_genre_id[0]
        self.bubble_sort(book_genre_id)
        if self.book_genre_id_ent.get() == "":
            messagebox.showerror("Unfulfilled Box", "Please fill ID box first!")
        else:
            try:
                if int(self.book_genre_id_ent.get()) not in book_genre_id:   # Searching
                    messagebox.showerror("Unmatched ID", "Please enter correct ID.")
                else:
                    book_genre = BookGenreDelete(self.book_genre_id_ent.get())
                    query = "delete from book_genres where Book_Genre_ID=%s;"
                    values = (book_genre.get_book_genre_id(),)
                    DbConnection().delete(query, values)
                    DbConnection().close()
                    messagebox.showinfo("Data delete complete", "One author is successfully deleted.")
                    self.book_genre_fetch_data()
            except ValueError:
                messagebox.showerror("Invalid Input ID", "Please enter number in ID.")

    # =======================================Method To clear Combo and Entries=======================================
    def author_clear1(self):
        self.author_search_combo.delete(0, END)
        self.author_search_ent.delete(0, END)

    def book_genre_clear1(self):
        self.book_genre_search_combo.delete(0, END)
        self.book_genre_search_ent.delete(0, END)

    # =======================================Method To clear Entries=======================================
    def author_clear(self):
        self.author_id_ent.delete(0, END)
        self.author_first_name_ent.delete(0, END)
        self.author_last_name_ent.delete(0, END)
        self.author_no_of_book_ent.delete(0, END)

    def book_genre_clear(self):
        self.book_genre_id_ent.delete(0, END)
        self.book_genre_name_combo.delete(0, END)
        self.book_genre_no_of_book_ent.delete(0, END)

    # =======================================Method To Open Old Window=======================================
    def old_window(self):
        ButtonsInterface(Toplevel())
        self.root.withdraw()


class AddBookInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Management System")
        self.root.geometry("1920x1080")

        self.img1 = ImageTk.PhotoImage(Image.open("Image/a1.jpg"))
        self.image_label = Label(self.root, image=self.img1)
        self.image_label.place(y=70)

    # =======================================Data List=======================================
        language = ("Nepali", "English", "Hindi", "Spanish", "French", "Russian", "Japanese", "Korean", "Chinese",
                    "German", "Urdu")
        author_query = "select Author_ID from authors;"
        author_data = DbConnection().select(author_query)
        book_genre_query = "select Book_Genre_ID from book_genres;"
        book_genre_data = DbConnection().select(book_genre_query)

    # =======================================Heading=======================================
        head_label = Label(self.root, text="Book Management System",
                           font=("cambria", 40, "bold"), bg="light blue", bd=5, relief=GROOVE)
        head_label.pack(side=TOP, fill=X)

    # =======================================Frame=======================================
        add_frame = Frame(self.root, bg="light blue", bd=5, relief=SUNKEN)
        add_frame.place(x=540, y=100, width=900, height=850)

        # ================================Frame's Labels================================
        add_label = Label(add_frame, text="Add Book Details", font=("cambria", 25, "bold"), bg="light blue")
        add_label.place(x=330, y=5)

        isbn_lbl = Label(add_frame, text="ISBN:", bg="light blue", font=("cambria", 25, "normal"))
        isbn_lbl.place(x=100, y=60)

        book_title_lbl = Label(add_frame, text="Book Title:", bg="light blue", font=("cambria", 25, "normal"))
        book_title_lbl.place(x=100, y=140)

        language_lbl = Label(add_frame, text="Language:", bg="light blue", font=("cambria", 25, "normal"))
        language_lbl.place(x=100, y=220)

        author_id_lbl = Label(add_frame, text="Author ID:", bg="light blue", font=("cambria", 25, "normal"))
        author_id_lbl.place(x=100, y=300)

        book_genre_id_lbl = Label(add_frame, text="Book Genre ID:", bg="light blue",
                                  font=("cambria", 25, "normal"))
        book_genre_id_lbl.place(x=100, y=380)

        publication_year_lbl = Label(add_frame, text="Publication Year:", bg="light blue",
                                     font=("cambria", 25, "normal"))
        publication_year_lbl.place(x=100, y=460)

        price_lbl = Label(add_frame, text="Price:", bg="light blue", font=("cambria", 25, "normal"))
        price_lbl.place(x=100, y=540)

        no_of_copies_lbl = Label(add_frame, text="No Of Copies:", bg="light blue", font=("cambria", 25, "normal"))
        no_of_copies_lbl.place(x=100, y=620)

        # ================================Frame's Entries================================
        self.isbn_ent = Entry(add_frame, font=("cambria", 25, "normal"), width=25, bd=3, relief=SUNKEN)
        self.isbn_ent.place(x=380, y=60)

        self.book_title_ent = Entry(add_frame, font=("cambria", 25, "normal"), width=25, bd=3, relief=SUNKEN)
        self.book_title_ent.place(x=380, y=140)

        self.language_combo = ttk.Combobox(add_frame, font=("cambria", 25, "normal"), width=24)
        self.language_combo['values'] = language
        self.language_combo.place(x=380, y=220)

        self.author_id_combo = ttk.Combobox(add_frame, font=("cambria", 25, "normal"), width=24)
        self.author_id_combo["values"] = author_data
        self.author_id_combo.place(x=380, y=300)

        self.book_genre_id_combo = ttk.Combobox(add_frame, font=("cambria", 25, "normal"), width=24)
        self.book_genre_id_combo["values"] = book_genre_data
        self.book_genre_id_combo.place(x=380, y=380)

        self.publication_year_ent = Entry(add_frame, font=("cambria", 25, "normal"), width=25, bd=3, relief=SUNKEN)
        self.publication_year_ent.place(x=380, y=460)

        self.price_ent = Entry(add_frame, font=("cambria", 25, "normal"), width=25, bd=3, relief=SUNKEN)
        self.price_ent.place(x=380, y=540)

        self.no_of_copies_ent = Entry(add_frame, font=("cambria", 25, "normal"), width=25, bd=3, relief=SUNKEN)
        self.no_of_copies_ent.place(x=380, y=620)

        # ================================Frame's Buttons================================
        add_btn = Button(add_frame, text="Add", font=("cambria", 20, "normal"), bg="dark orange",
                         width=8, command=self.add)
        add_btn.place(x=250, y=730)

        author_clear_btn = Button(add_frame, text="clear", font=("cambria", 20, "normal"), bg="light blue",
                                  width=8, command=self.clear)
        author_clear_btn.place(x=550, y=730)

        back_btn = Button(self.root, text="Back", font=("cambria", 15, "normal"), width=15, bg="blue",
                          command=self.old_window)
        back_btn.place(x=860, y=990)

    # =======================================Method To Add Data======================================
    def add(self):
        query = "select * from books;"
        data = DbConnection().select(query)
        isbn = []
        for row in data:
            isbn.append(row[0])
        try:
            if self.isbn_ent.get() == "" or self.book_title_ent.get() == "" or self.language_combo.get() == "" or \
                    self.author_id_combo.get() == "" or self.book_genre_id_combo.get() == "" or \
                    self.publication_year_ent.get() == "" or self.price_ent.get() == "" or \
                    self.no_of_copies_ent.get() == "":
                messagebox.showerror("Unfulfilled Boxes", "Please fill all the boxes first!")
            else:
                try:
                    a = int(self.book_title_ent.get())
                    messagebox.showerror("Invalid Input", "Please! Enter letters in 'Book Title'.")
                except ValueError:
                    b = int(self.language_combo.get())
                    messagebox.showerror("Invalid Input", "Please! Enter letters in 'Language'.")
        except ValueError:
            try:
                if int(self.isbn_ent.get()) == int or int(self.author_id_combo.get()) == int or \
                        int(self.book_genre_id_combo.get()) == int or int(self.publication_year_ent.get()) == int or \
                        int(self.price_ent.get()) == int or int(self.no_of_copies_ent.get()) == int:
                    a = True
            except ValueError:
                messagebox.showerror("Invalid Input",
                                     "Please! Enter number in ISBN, Author ID, Book Genre ID,"
                                     " Publication Year and No Of Copies.")
            else:
                if self.isbn_ent.get() in isbn:   # Searching
                    messagebox.showerror("ISBN Matched", "You can not add a book having same ISBN.")
                else:
                    book = BookADDUpdate(self.isbn_ent.get(), self.book_title_ent.get(), self.language_combo.get(),
                                         self.author_id_combo.get(), self.book_genre_id_combo.get(),
                                         self.publication_year_ent.get(), self.price_ent.get(),
                                         self.no_of_copies_ent.get())
                    query = "insert into books values(%s, %s, %s, %s, %s, %s, %s, %s);"
                    values = (book.get_isbn(), book.get_book_title(), book.get_language(), int(book.get_author_id()),
                              int(book.get_book_genre_id()), book.get_publication_year(), "Rs." + book.get_price(),
                              book.get_no_of_copies())
                    DbConnection().add(query, values)
                    DbConnection().close()
                    messagebox.showinfo("Data addition complete", "One book is successfully added.")

    # =======================================Method To clear Entries=======================================
    def clear(self):
        self.isbn_ent.delete(0, END)
        self.book_title_ent.delete(0, END)
        self.language_combo.delete(0, END)
        self.author_id_combo.delete(0, END)
        self.book_genre_id_combo.delete(0, END)
        self.publication_year_ent.delete(0, END)
        self.price_ent.delete(0, END)
        self.no_of_copies_ent.delete(0, END)

    # =======================================Method To Open Old Window=======================================
    def old_window(self):
        ButtonsInterface(Toplevel())
        self.root.withdraw()


class AddAuthorBookGenreInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Management System")
        self.root.geometry("1920x1080")

        self.img1 = ImageTk.PhotoImage(Image.open("Image/a5.jpg"))
        self.image_label = Label(self.root, image=self.img1)
        self.image_label.place(y=70)

    # =======================================Heading=======================================
        head_label = Label(self.root, text="Book Management System",
                           font=("cambria", 40, "bold"), bg="light blue", bd=5, relief=GROOVE)
        head_label.pack(side=TOP, fill=X)

    # =======================================Frame's Frames=======================================
        author_add_frame = Frame(self.root, bg="light blue", bd=5, relief=SUNKEN)
        author_add_frame.place(x=80, y=200, width=800, height=600)

        book_genre_add_frame = Frame(self.root, bg="light blue", bd=5, relief=SUNKEN)
        book_genre_add_frame.place(x=1030, y=250, width=800, height=500)

        # ================================Frame Frame's Labels================================
        # =======================================Author=======================================
        author_add_lbl = Label(author_add_frame, text="Add Authors", font=("cambria", 20, "bold"), bg="light blue")
        author_add_lbl.place(x=280, y=20)

        author_id_lbl = Label(author_add_frame, text="ID:", bg="light blue",
                              font=("cambria", 25, "normal"))
        author_id_lbl.place(x=50, y=100)

        author_first_name_lbl = Label(author_add_frame, text="First Name:", bg="light blue",
                                      font=("cambria", 25, "normal"))
        author_first_name_lbl.place(x=50, y=200)

        author_last_name_lbl = Label(author_add_frame, text="Last Name:", bg="light blue",
                                     font=("cambria", 25, "normal"))
        author_last_name_lbl.place(x=50, y=300)

        author_no_of_book_lbl = Label(author_add_frame, text="No Of Books:", bg="light blue",
                                      font=("cambria", 25, "normal"))
        author_no_of_book_lbl.place(x=50, y=400)

        # =======================================Book Genre=======================================
        book_genre_add_lbl = Label(book_genre_add_frame, text="Add Book Genres", font=("cambria", 20, "bold"),
                                   bg="light blue",)
        book_genre_add_lbl.place(x=280, y=20)

        book_genre_id_lbl = Label(book_genre_add_frame, text="ID:", bg="light blue",
                                  font=("cambria", 25, "normal"))
        book_genre_id_lbl.place(x=50, y=100)

        book_genre_name_lbl = Label(book_genre_add_frame, text="Book Genre Name:", bg="light blue",
                                    font=("cambria", 25, "normal"))
        book_genre_name_lbl.place(x=50, y=200)

        book_genre_no_of_book_lbl = Label(book_genre_add_frame, text="No Of Books:", bg="light blue",
                                          font=("cambria", 25, "normal"))
        book_genre_no_of_book_lbl.place(x=50, y=300)

        # ================================Frame Frame's Entries================================
        # =======================================Author=======================================
        self.author_id_ent = Entry(author_add_frame, font=("cambria", 25, "normal"), bd=3, relief=SUNKEN)
        self.author_id_ent.place(x=250, y=100)

        self.author_first_name_ent = Entry(author_add_frame, font=("cambria", 25, "normal"), bd=3, relief=SUNKEN)
        self.author_first_name_ent.place(x=250, y=200)

        self.author_last_name_ent = Entry(author_add_frame, font=("cambria", 25, "normal"), bd=3, relief=SUNKEN)
        self.author_last_name_ent.place(x=250, y=300)

        self.author_no_of_book_ent = Entry(author_add_frame, font=("cambria", 25, "normal"), bd=3, relief=SUNKEN)
        self.author_no_of_book_ent.place(x=250, y=400)

        # =======================================Book Genre=======================================
        self.book_genre_id_ent = Entry(book_genre_add_frame, font=("cambria", 25, "normal"), bd=3, relief=SUNKEN)
        self.book_genre_id_ent.place(x=350, y=100)

        self.book_genre_name_combo = ttk.Combobox(book_genre_add_frame, font=("cambria", 25, "normal"), width=19)
        self.book_genre_name_combo["values"] = ('Action and Adventure', 'Art/Architecture', 'Biography',
                                                'Business/Economics', "Children's", 'Comic Book', 'Crime', 'Cultural',
                                                'Diary', 'Dictionary', 'Drama', 'Encyclopedia', 'Graphic novel',
                                                'Guide', 'Health', 'History', 'Horror', 'Humor', 'Journal', 'Math',
                                                'Mystery', 'Poetry', 'Review', 'Romance', 'Science', 'Science Fiction',
                                                'Sports', 'Story', 'Thriller', 'Travel')
        self.book_genre_name_combo.place(x=350, y=200)

        self.book_genre_no_of_book_ent = Entry(book_genre_add_frame,
                                               font=("cambria", 25, "normal"), bd=3, relief=SUNKEN)
        self.book_genre_no_of_book_ent.place(x=350, y=300)

        # ================================Frame Frame's Buttons================================
        # ================================Author================================
        author_add_btn = Button(author_add_frame, text="Add", font=("cambria", 20, "normal"), bg="dark orange",
                                width=8, command=self.author_add)
        author_add_btn.place(x=180, y=500)

        author_author_clear_btn = Button(author_add_frame, text="clear", font=("cambria", 20, "normal"), bg="light blue",
                                         width=8, command=self.author_clear)
        author_author_clear_btn.place(x=480, y=500)

        # ================================Book Genre================================
        book_genre_add_btn = Button(book_genre_add_frame, text="Add", font=("cambria", 20, "normal"), bg="dark orange",
                                    width=8, command=self.book_genre_add)
        book_genre_add_btn.place(x=180, y=400)

        book_genre_author_clear_btn = Button(book_genre_add_frame, text="clear", font=("cambria", 20, "normal"),
                                             bg="light blue", width=8, command=self.book_genre_clear)
        book_genre_author_clear_btn.place(x=480, y=400)

        back_btn = Button(self.root, text="Back", font=("cambria", 15, "normal"), width=15, bg="blue",
                          command=self.old_window)
        back_btn.place(x=860, y=940)

    # =======================================Method To Add Data======================================
    def author_add(self):
        query = "select * from authors;"
        data = DbConnection().select(query)
        author_id = []
        if len(data) != 0:
            for row in data:
                author_id.append(row[0])
        try:
            if self.author_id_ent.get() == "" or self.author_first_name_ent.get() == "" or \
                    self.author_last_name_ent.get() == "" or self.author_no_of_book_ent.get() == "":
                messagebox.showerror("Unfulfilled Boxes", "Please fill all the boxes first!")
            else:
                try:
                    a = int(self.author_first_name_ent.get())
                    messagebox.showerror("Invalid Input", "Please! Enter letters in 'Author first name'.")
                except ValueError:
                    b = int(self.author_last_name_ent.get())
                    messagebox.showerror("Invalid Input", "Please! Enter letters in 'Author last name'.")
        except ValueError:
            try:
                if int(self.author_id_ent.get()) == int or int(self.author_no_of_book_ent.get()) == int:
                    a = True
            except ValueError:
                messagebox.showerror("Invalid Input",
                                     "Please! Enter number in Author ID and No of Books.")
            else:
                if int(self.author_id_ent.get()) in author_id:  # Searching
                    messagebox.showerror("ID Matched", "You can not add a author having same ID.")
                else:
                    author = AuthorAddUpdate(self.author_id_ent.get(), self.author_first_name_ent.get(),
                                             self.author_last_name_ent.get(), self.author_no_of_book_ent.get())
                    query = "insert into authors values(%s, %s, %s, %s);"
                    values = (author.get_author_id(), author.get_author_first_name(), author.get_author_last_name(),
                              author.get_no_of_books())
                    DbConnection().add(query, values)
                    DbConnection().close()
                    messagebox.showinfo("Data addition complete", "One Author is successfully added.")

    def book_genre_add(self):
        query = "select * from book_genres;"
        data = DbConnection().select(query)
        book_genre_id = []
        if len(data) != 0:
            for row in data:
                book_genre_id.append(row[0])
        try:
            if self.book_genre_id_ent.get() == "" or self.book_genre_name_combo.get() == "" or \
                   self.book_genre_no_of_book_ent.get() == "":
                messagebox.showerror("Unfulfilled Boxes", "Please fill all the boxes first!")
            else:
                a = int(self.book_genre_name_combo.get())
                messagebox.showerror("Invalid Input", "Please! Enter letters in 'Book Genre name'.")
        except ValueError:
            try:
                if int(self.book_genre_id_ent.get()) == int or int(self.book_genre_no_of_book_ent.get()) == int:
                    a = True
            except ValueError:
                messagebox.showerror("Invalid Input",
                                     "Please! Enter number in Book Genre ID and No of Books.")
            else:
                if int(self.book_genre_id_ent.get()) in book_genre_id:  # Searching
                    messagebox.showerror("ID Matched", "You can not add a Book genre having same ID.")
                else:
                    book_genre = BookGenreAddUpdate(self.book_genre_id_ent.get(), self.book_genre_name_combo.get(),
                                                    self.book_genre_no_of_book_ent.get())
                    query = "insert into book_genres values(%s, %s, %s);"
                    values = (book_genre.get_book_genre_id(), book_genre.get_book_genre_name(),
                              book_genre.get_no_of_books())
                    DbConnection().add(query, values)
                    DbConnection().close()
                    messagebox.showinfo("Data addition complete", "One Book Genre is successfully added.")

    # =======================================Method To clear Entries=======================================
    def author_clear(self):
        self.author_id_ent.delete(0, END)
        self.author_first_name_ent.delete(0, END)
        self.author_last_name_ent.delete(0, END)
        self.author_no_of_book_ent.delete(0, END)

    def book_genre_clear(self):
        self.book_genre_id_ent.delete(0, END)
        self.book_genre_name_combo.delete(0, END)
        self.book_genre_no_of_book_ent.delete(0, END)

    # =======================================Method To Open Old Window=======================================
    def old_window(self):
        ButtonsInterface(Toplevel())
        self.root.withdraw()


Window = Tk()
LoginInterface(Window)
Window.mainloop()