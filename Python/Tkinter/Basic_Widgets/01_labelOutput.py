Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> label = ttk.Label(root, text = "Hello, Tkinter!")
>>> label.pack()
>>> label.config(text = 'Howdy, Tkinter!')
>>> label.config(text = 'Howdy, Tkinter! It\'s been a really long time since we last met.  Great to see you again!')
>>> label.config(wraplength = 150)
>>> label.config(justify = CENTER)
>>> label.config(foreground = 'blue', background = 'yellow')
>>> label.config(font = ('Courier', 18, 'bold'))
>>> label.config(text = 'Howdy, Tkinter!')
>>> logo = PhotoImage(file = 'python_logo.gif')
>>> label.config(image = logo)
>>> label.config(compound = 'text')
>>> label.config(compound = 'center')
>>> label.config(compound = 'left')
>>> label.img = logo
>>> label.config(image = label.img)
>>> root.mainloop()
