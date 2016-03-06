Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import tkinter
>>> import _tkinter
>>> tkinter._test()
>>> 
 RESTART: C:\Python35\Python3 - Tech Academy\Tkinter_Exercise Files\Ch01\05_hello_tkinter.py 
>>> from tkinter immport *
SyntaxError: invalid syntax
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> button = ttk.Button(root, text = 'Click me')
>>> button.pack()
>>> button['text']
'Click me'
>>> button['text'] = 'Press Me'
>>> button.config(text = 'Push Me')
>>> button.config()
{'image': ('image', 'image', 'Image', '', ''), 'style': ('style', 'style', 'Style', '', ''), 'cursor': ('cursor', 'cursor', 'Cursor', '', ''), 'padding': ('padding', 'padding', 'Pad', '', ''), 'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', 'ttk::takefocus', 'ttk::takefocus'), 'state': ('state', 'state', 'State', <index object: 'normal'>, <index object: 'normal'>), 'underline': ('underline', 'underline', 'Underline', -1, -1), 'default': ('default', 'default', 'Default', <index object: 'normal'>, <index object: 'normal'>), 'compound': ('compound', 'compound', 'Compound', <index object: 'none'>, <index object: 'none'>), 'class': ('class', '', '', '', ''), 'width': ('width', 'width', 'Width', '', ''), 'command': ('command', 'command', 'Command', <bytecode object: ''>, <bytecode object: ''>), 'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''), 'text': ('text', 'text', 'Text', '', 'Push Me')}
>>> str(button)
'.2059962408520'
>>> str(root)
'.'
>>> ttk.Label(root, text = 'hello Tkinter').pack()
>>> 
