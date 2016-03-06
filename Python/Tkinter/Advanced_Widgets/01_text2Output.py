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
>>> text.tag_add('my_tag', '1.0', '1.0 wordend')
>>> text.tag_configure('my_tag', background = 'yellow')
>>> text.tag_remove('my_tag', '1.1', '1.3')
>>> print(text.tag_ranges('my_tag'))
(<textindex object: '1.0'>, <textindex object: '1.1'>, <textindex object: '1.3'>, <textindex object: '1.4'>)
>>> print(text.tag_names())
('sel', 'my_tag')
>>> text.replace('my_tag.first', 'my_tag.last', 'That was')
>>> text.tag_delete('my_tag')
>>> 
>>> text.mark_names()
('insert', 'current', 'tk::anchor1')
>>> text.insert('insert', '_')
>>> text.mark_set('my_mark', 'end')
>>> text.mark_gravity('my_mark', 'right')
''
>>> text.mark_unset('my_mark')
>>> 
>>> image = PhotoImage(file = 'C:\\Python35\Python3 - Tech Academy\Tkinter_Exercise Files\Ch04 - Organizational Widgets python_logo.gif').subsample(5, 5) # Change path as needed

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    image = PhotoImage(file = 'C:\\Python35\Python3 - Tech Academy\Tkinter_Exercise Files\Ch04 - Organizational Widgets python_logo.gif').subsample(5, 5) # Change path as needed
  File "C:\Python35\lib\tkinter\__init__.py", line 3393, in __init__
    Image.__init__(self, 'photo', name, cnf, master, **kw)
  File "C:\Python35\lib\tkinter\__init__.py", line 3349, in __init__
    self.tk.call(('image', 'create', imgtype, name,) + options)
_tkinter.TclError: couldn't open "C:\Python35\Python3 - Tech Academy\Tkinter_Exercise Files\Ch04 - Organizational Widgets python_logo.gif": no such file or directory
>>> image = PhotoImage(file = 'C:\\Python35\\Python3 - Tech Academy\\Tkinter_Exercise Files\\Ch04 - Organizational Widgets\\python_logo.gif').subsample(5, 5)
>>> text.image_create('insert', image = image)
'pyimage3'
>>> button = Button(text, text = 'Click Me')
>>> text.window_create('insert', window = button)
>>> 
