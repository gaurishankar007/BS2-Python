from tkinter import *
from tkinter import messagebox
import sys

# Creating Window
Window = Tk()
Window.geometry('500x300+800+300')
Window.title("Python Gui Tkinter")

# Adding widget in window
# pack property == side(LEFT, RIGHT, TOP, BOTTOM) and padx(7, 9, 3) and pady(2, 6 8)
Btn1 = Button(Window, text="Click 1", width=10, height=2, bd=5, padx=4, pady=10, fg="dark blue", bg="pink",
              activebackground="blue", relief=GROOVE)
Btn1.pack(side=TOP, pady=10)

Btn2 = Button(Window, text="Click 2", width=10, height=2, bd=5, fg="dark blue", bg="pink", justify=LEFT
              , relief=SUNKEN)
Btn2.pack(side=LEFT)

Btn3 = Button(Window, text="Click 3", width=10, height=2, bd=5, fg="dark blue", bg="pink", relief=GROOVE)
Btn3.pack(side=RIGHT)

Btn4 = Button(Window, text="Click 4", width=10, height=2, bd=5, fg="dark blue", bg="pink", justify=RIGHT, relief=GROOVE)
Btn4.pack(side=BOTTOM, padx=5)

Window.mainloop()

# Creating Another Window1
Window1 = Tk()
Window1.geometry('500x300+800+300')
Window1.title("Python Gui Tkinter")

Btn1 = Button(Window1, text="Click 1", width=10, height=2, bd=5, fg="dark blue", bg="red", activebackground="blue",
              relief=GROOVE)
Btn1.grid(row=0, column=0, padx=5, pady=5)

Btn2 = Button(Window1, text="Click 2", width=10, height=2, bd=5, fg="dark blue", bg="red", justify=LEFT
              , relief=SUNKEN)
Btn2.grid(row=0, column=1, padx=5, pady=5)

Btn3 = Button(Window1, text="Click 3", width=10, height=2, bd=5, fg="dark blue", bg="red", relief=GROOVE)
Btn3.grid(row=1, column=0, padx=5, pady=5)

Btn4 = Button(Window1, text="Click 4", width=10, height=2, bd=5, fg="dark blue", bg="red", justify=RIGHT, relief=GROOVE)
Btn4.grid(row=1, column=1, padx=5, pady=5)

Window1.mainloop()


# Creating Another Window2
Window2 = Tk()
Window2.geometry('500x300+800+300')
Window2.title("Python Gui Tkinter")


def click_handle(event):
    messagebox.showinfo("Message", "Oh!, you have clicked the button.")


def double_click(e):
    messagebox.showinfo("Message", "Oh!, you have double clicked the button.")
    sys.exit()


def exit_click(e):
    sys.exit()


Btn1 = Button(Window2, text="Click 1", width=10, height=2, bd=5, fg="dark blue", bg="red", activebackground="blue",
              relief=GROOVE)
Btn1.place(x=20, y=30)
Btn1.bind("<Button-1>", click_handle)  # While clicking mouse left button

Btn2 = Button(Window2, text="Close", width=10, height=2, bd=5, fg="dark blue", bg="red", activebackground="green", justify=LEFT
              , relief=SUNKEN)
Btn2.place(x=150, y=100)
Btn2.bind("<Double-1>", double_click)  # While double clicking the mouse left button

Btn3 = Button(Window2, text="Click 3", width=10, height=2, bd=5, fg="dark blue", bg="red", relief=GROOVE)
Btn3.place(x=250, y=10)

Btn4 = Button(Window2, text="Click 4", width=10, height=2, bd=5, fg="dark blue", bg="red", justify=RIGHT, relief=GROOVE)
Btn4.place(x=400, y=40)
Btn4.bind("<Double-1>", exit_click)  # While double clicking the mouse left button

Ent = Entry(Window2, text="", fg="dark blue", bg="red")
Ent.place(x=300, y=200)

Window2.mainloop()

# Creating Another Window3
Window3 = Tk()
Window3.geometry('500x300+800+300')
Window3.title("Bind Mouse Movement Example")


def mouse_movement(parameter):
    print("mouse is at x:y(%s, %s)" % (parameter.x, parameter.y))
    messagebox.showinfo("Mouse x:y Coordinate", "mouse is at x:y(%s, %s)" % (parameter.x, parameter.y))


Btn1 = Button(Window3, text="Mouse Movement", width=20, height=3, bd=5, fg="dark blue", bg="red", activebackground="blue",
              relief=GROOVE, font=("arial", 12, "bold"))
Btn1.pack(pady=100)
Btn1.bind("<Motion>", mouse_movement)

Window3.mainloop()

# Creating Another Window4
Window4 = Tk()
Window4.geometry('500x300+800+300')
Window4.title("Command Example")


def event_handle(name):
    messagebox.showinfo("Message Showing", f"Your name is {name}.")


def event_handle1():
    messagebox.showinfo("Message Showing", "You have clicked the button.")


Btn1 = Button(Window4, text="Click 1", width=20, height=3, bd=5, fg="white", bg="blue", activebackground="light blue",
              relief=GROOVE, font=("arial", 12, "bold"), command=lambda: event_handle("Gauri"))
Btn1.pack()

Btn2 = Button(Window4, text="Click 2", width=20, height=3, bd=5, fg="white", bg="blue", activebackground="light blue",
              relief=GROOVE, font=("arial", 12, "bold"), command=event_handle1)
Btn2.pack()


Window4.mainloop()