Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> 
>>> root = Tk()
>>> 
>>> notebook = ttk.Notebook(root)
>>> notebook.pack()
>>> 
>>> frame1 = ttk.Frame(notebook)
>>> frame2 = ttk.Frame(notebook)
>>> notebook.add(frame1, text = 'One')
>>> notebook.add(frame2, text = 'Two')
>>> ttk.Button(frame1, text = 'Click Me').pack()
>>> 
>>> frame3 = ttk.Frame(notebook)
>>> notebook.insert(1, frame3, text = 'Three')
>>> notebook.forget(1)
>>> notebook.add(frame3, text = 'Three')
>>> 
>>> print(notebook.select())
.2931030548264.2931030548040
>>> print(notebook.index(notebook.select()))
0
>>> notebook.select(2)
''
>>> 
>>> notebook.tab(1, state = 'disabled')
{}
>>> notebook.tab(1, state = 'hidden')
{}
>>> notebook.tab(1, state = 'normal')
{}
>>> notebook.tab(1, 'text')
'Two'
>>> notebook.tab(1)
{'padding': [0], 'text': 'Two', 'sticky': 'nsew', 'image': '', 'compound': 'none', 'state': 'normal', 'underline': -1}
>>> 
