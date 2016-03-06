Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> 
>>> frame = ttk.Frame(root)
>>> frame.pack()
>>> frame.config(height = 100, width = 200)
>>> frame.config(relief = RIDGE)
>>> ttk.Button(frame, text = 'Click Me').grid()
>>> frame.config(padding = (30, 15))
>>> ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()
>>> 
