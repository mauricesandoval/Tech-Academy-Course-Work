Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> button = ttk.Button(root, text = "Click Me")
>>> button.pack()
>>> def callback():
	print('Clicked!')

	
>>> button.config(command = callback)
>>> Clicked!
Clicked!
Clicked!
Clicked!
Clicked!
Clicked!Clicked!
SyntaxError: invalid syntax
>>> button.invoke()
Clicked!
'None'
>>> button.state(['disabled'])
('!disabled',)
>>> print(button.instate(['disabled']))
True
>>> button.state(['!disabled'])
('disabled',)
>>> Clicked!
Clicked!
SyntaxError: invalid syntax
>>> 
>>> print(button.instate(['!disabled']))
True
>>> logo = PhotoImage(file = 'C:\\Python35\python_logo.gif')
>>> Clicked!
Clicked!
SyntaxError: invalid syntax
>>> button.config(image = logo, compound = LEFT)
>>> Clicked!
Clicked!
Clicked!
SyntaxError: invalid syntax
>>> small_logo = logo.subsample(5, 5)
>>> button.config(image = small_logo)
>>> root.mainloop()
Clicked!
