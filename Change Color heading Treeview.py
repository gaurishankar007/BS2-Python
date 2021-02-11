from tkinter import *
from tkinter import ttk


class Interface:
    def __init__(self, window):
        self.window = window
        self.window.title("My first GUI")
        self.window.geometry("200x200")

        style = ttk.Style()
        style.element_create("Custom.Treeheading.border", "from", "default")
        style.layout("Custom.Treeview.Heading", [
            ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
            ("Custom.Treeheading.border", {'sticky': 'nswe', 'children': [
                ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
                    ("Custom.Treeheading.image", {'side': 'right', 'sticky': ''}),
                    ("Custom.Treeheading.text", {'sticky': 'we'})
                ]})
            ]}),
        ])
        style.configure("Custom.Treeview.Heading",
                        background="green", foreground="white", relief="flat")
        style.map("Custom.Treeview.Heading",
                  relief=[('active', 'groove'), ('pressed', 'sunken')])

        # create Treeview datagridview
        self.tv = ttk.Treeview(self.window, height=8, style="Custom.Treeview")
        # self.tv.grid(row=3, column=0)
        self.tv['columns'] = ('id', 'symbol', 'price', 'trigger', 'shares', 'side', 'type', 'status', 'fill')
        self.tv.heading("#0", text='Time', anchor='w')
        self.tv.column("#0", stretch=NO, width=5, anchor="w")
        self.tv.heading('id', text='ID')
        self.tv.column('id', anchor='center', width=70)
        self.tv.heading('symbol', text='Symbol')
        self.tv.column('symbol', anchor='center', width=70)
        self.tv.heading('price', text='Price')
        self.tv.column('price', anchor='center', width=70)
        self.tv.heading('trigger', text='Trigger')
        self.tv.column('trigger', anchor='center', width=70)
        self.tv.heading('shares', text='Shares')
        self.tv.column('shares', anchor='center', width=100)
        self.tv.heading('side', text='Side')
        self.tv.column('side', anchor='center', width=70)
        self.tv.heading('type', text='Type')
        self.tv.column('type', anchor='center', width=70)
        self.tv.heading('status', text='Status')
        self.tv.column('status', anchor='center', width=100)
        self.tv.heading('fill', text='Fill')
        self.tv.column('fill', anchor='center', width=70)
        self.tv.grid(row=1, column=0, columnspan=6, padx=5, pady=5)
        self.treeview = self.tv


window = Tk()
Interface(window)
window.mainloop()