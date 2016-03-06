Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> 
>>> root.option_add('*tearOff', False)
>>> menubar = Menu(root)
>>> root.config(menu = menubar)
>>> file = Menu(menubar)
>>> edit = Menu(menubar)
>>> help_ = Menu(menubar)
>>> 
>>> menubar.add_cascade(menu = file, label = 'File')
>>> menubar.add_cascade(menu = edit, label = 'Edit')
>>> menubar.add_cascade(menu = help_, label = 'Help')
>>> 
>>> file.add_command(label = 'New', command = lambda: print('New File'))
>>> New File
New File
SyntaxError: invalid syntax
>>> file.add_separator()
>>> file.add_command(label = 'Open...', command = lambda: print('Opening File...'))
>>> file.add_command(label = 'Save', command = lambda: print('Saving File...'))
>>> Opening File...
Saving File...

>>> file.entryconfig('New', accelerator = 'Ctrl+N')
>>> logo = PhotoImage(file = 'C:\\Python35\Python3 - Tech Academy\\Tkinter_Exercise Files\\Ch05 - Advanced Widgets\\python_logo.gif').subsample(10, 10)
>>> file.entryconfig('Open...', image = logo, compound = 'left')
>>> Opening File...

>>> file.entryconfig('Open...', state = 'disabled')
>>> 
>>> file.delete('Save')
>>> save = Menu(file)
>>> file.add_cascade(menu = save, label = 'Save')
>>> save.add_command(label = 'Save As',command = lambda: print('Saving As...'))
>>> Saving As...

>>> save.add_command(label = 'Save All', command = lambda: print('Saving All...'))
>>> Saving All...

>>> choice = IntVar()
>>> edit.add_radiobutton(label = 'One', variable = choice, value = 1)
>>> edit.add_radiobutton(label = 'Two', variable = choice, value = 2)
>>> edit.add_radiobutton(label = 'Three', variable = choice, value = 3)
>>> file.post(400, 300)
>>> 
