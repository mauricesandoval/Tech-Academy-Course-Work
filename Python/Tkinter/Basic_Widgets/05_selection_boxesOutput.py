Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> month = StringVar()
>>> combobox = ttk.Combobox(root, textvariable = month)
>>> combobox.pack()
>>> combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
>>> print(month.get())

>>> print(month.get())
May
>>> print(month.get())
Feb
>>> month.set('Dec')
>>> month.set('Not a month!')
>>> print(month.get())
whatever is clever
>>> year = StringVar()
>>> Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack()
>>> print(year.get())
2000
>>> root.mainloop()
