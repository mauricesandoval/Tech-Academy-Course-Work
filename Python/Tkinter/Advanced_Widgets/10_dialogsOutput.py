Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import messagebox
>>> 
>>> messagebox.showinfo(title = "A Friendly Message", message = 'Hello, Tkinter!')
'ok'
>>> print(messagebox.askyesno(title = 'Hungry?', message = 'Do you want SPAM?'))
True
>>> 
>>> from tkinter import filedialog
>>> filename = filedialog.askopenfile()
>>> 
>>> from tkinter import colorchooser
>>> print(colorchooser.askcolor(initialcolor = "#FFFFFF"))
(None, None)
>>> 
