Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> checkbutton = ttk.Checkbutton(root, text = 'SPAM?')
>>> checkbutton.pack()
>>> spam = StringVar()
>>> spam.set('SPAM!')
>>> print(spam.get())
SPAM!
>>> checkbutton.config(variable = spam, onvalue = 'SPAM Please!',
		   offvalue = 'Boo SPAM!')
>>> print(spam.get())
SPAM Please!
>>> print(spam.get())
Boo SPAM!
>>> breakfast = StringVar()
>>> ttk.Radiobutton(root, text = 'SPAM', variable = breakfast,
		value = 'SPAM').pack()
>>> 
>>> ttk.Radiobutton(root, text = 'Eggs', variable = breakfast,
		value = 'Eggs').pack()
>>> ttk.Radiobutton(root, text = 'Sausage', variable = breakfast,
		value = 'Sausage').pack()
>>> ttk.Radiobutton(root, text = 'SPAM', variable = breakfast,
		value = 'SPAM').pack()
>>> print(breakfast.get())
Sausage
>>> print(breakfast.get())
SPAM
>>> checkbutton.config(textvariable = breakfast)
>>> root.mainloop()
