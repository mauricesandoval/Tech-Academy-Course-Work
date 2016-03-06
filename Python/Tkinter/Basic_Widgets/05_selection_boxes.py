#!/usr/bin/python3

# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# Making selections with the combo box and spin box


from tkinter import *
from tkinter import ttk        
    
root = Tk()

month = StringVar()
combobox = ttk.Combobox(root, textvariable = month)
combobox.pack()
combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(month.get())
month.set('Dec')
month.set('Not a month!')

year = StringVar()
Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack()
print(year.get())

root.mainloop()
