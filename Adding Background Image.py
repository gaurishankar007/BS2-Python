from tkinter import *
from PIL import ImageTk, Image

app = Tk()
app.title("Welcome")

image = ImageTk.PhotoImage(Image.open("C:/Users/Gouri/Learning Python/a2.jpg"))
w = image.width()
h = image.height()
app.geometry("%dx%d" % (w, h))
lbl = Label(app, image=image)
lbl.pack()

app.mainloop()

# On Canvas
app1 = Tk()
c = Canvas(app1, bg="blue", height=800, width=1800)
c.pack()

img1 = ImageTk.PhotoImage(Image.open("C:/Users/Gouri/Learning Python/a2.jpg"))

c.create_image(20, 20, anchor=NW, image=img1)
app1.mainloop()