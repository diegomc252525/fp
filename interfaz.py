from tkinter import ttk
from tkinter import *

import sqlite3

class Product:

	def __init__(self, window):
		self.wind=window
		self.wind.title("Products Aplication")
		
		frame = LabelFrame(self.wind, text="register product")
		frame.grid(row=0,column=0,columnspan=3,pady=20)

		Label(frame,text ="name: ").grid(row=1,column=0)
		self.name = Entry(frame)
		self.name.focus()
		self.name.grid(row=1,column=1)

		Label(frame,text="Price: ").grid(row=2,column=0)
		self.price = Entry(frame)
		self.price.grid(row=2,column=1)

		ttk.Button(frame, text="save product").grid(row=3,columnspan=2,sticky=W + E)

		self.tree = ttk.Treeview(height=10,columns=2)
		self.tree.grid(row=4,column=0,columnspan=2)
		self.tree.heading("#0",text="name",anchor=CENTER)



if __name__ == '__main__':
	window = Tk()
	application = Product(window)
	window.mainloop()