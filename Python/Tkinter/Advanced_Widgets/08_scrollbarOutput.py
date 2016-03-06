Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> text = Text(root, width = 40, height = 10, wrap = 'word')
>>> text.grid(row = 0, column = 0)
>>> scrollbar = ttk.Scrollbar(root, orient = VERTICAL, command = text.yview)
>>> scrollbar.grid(row = 0, column = 1, sticky = 'ns')
>>> text.config(yscrollcommand = scrollbar.set)
>>> 
