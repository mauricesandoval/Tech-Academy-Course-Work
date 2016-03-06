Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> root = Tk()
>>> text = Text(root, width = 40, height = 10)
>>> text.pack()
>>> text.config(wrap = 'word')
>>> print(text.get('1.0', 'end'))
this is a display of the text wrap. It will show you example







if it hits the bottom of the text box, it will run off

>>> print(text.get('1.0', '1.end'))
this is a display of the text wrap. It will show you example
>>> text.insert('1.0 + 2 lines', 'Inserted message')
>>> text.insert('1.0 + 2 lines lineend', ' and\nmore and\nmore.')
>>> text.delete('1.0')
>>> text.delete('1.0', '1.0 lineend')
>>> text.delete('1.0', '3.0 lineend + 1 chars')
>>> text.replace('1.0', '1.0 lineend', 'This is the first line.')
>>> 
>>> text.config(state = 'disabled')
>>> text.delete('1.0', 'end')
>>> text.config(state = 'normal')
>>> 
