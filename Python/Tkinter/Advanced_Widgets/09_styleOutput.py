Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> 
>>> button1 = ttk.Button(root, text = 'Button 1')
>>> button2 = ttk.Button(root, text = 'Button 2')
>>> button1.pack()
>>> button2.pack()
>>> 
>>> style = ttk.Style()
>>> 
>>> print(style.theme_names())
('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
>>> print(style.theme_use())
vista
>>> style.theme_use('classic')
>>> style.theme_use('vista')
>>> 
>>> print(button1.winfo_class())
TButton
>>> style.configure('TButton', foreground = 'blue')
{}
>>> style.configure('Alarm.TButton', foreground = 'orange', font = ('Arial', 24, 'bold'))
{}
>>> button2.configure(style = 'Alarm.TButton')
>>> style.map('Alarm.TButton', foreground = [('pressed', 'pink'('disabled', 'grey')])
	  
SyntaxError: invalid syntax
>>> style.map('Alarm.TButton', foreground = [('pressed', 'pink'), ('disabled', 'grey')])
{}
>>> button2.state(['disabled'])
('!disabled',)
>>> 
>>> print(style.layout('TButton'))
[('Button.button', {'sticky': 'nswe', 'children': [('Button.focus', {'sticky': 'nswe', 'children': [('Button.padding', {'sticky': 'nswe', 'children': [('Button.label', {'sticky': 'nswe'})]})]})]})]
>>> print(style.element_options('Button.label'))
('-compound', '-space', '-text', '-font', '-foreground', '-underline', '-width', '-anchor', '-justify', '-wraplength', '-embossed', '-image', '-stipple', '-background')
>>> print(style.lookup('TButton', 'foreground'))
blue
>>> 
