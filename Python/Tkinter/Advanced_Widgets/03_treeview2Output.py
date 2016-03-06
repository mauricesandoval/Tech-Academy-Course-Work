Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> 
>>> treeview = ttk.Treeview(root)
>>> treeview.pack()
>>> treeview.insert('', '0', 'Item1', text = 'First Item')
'Item1'
>>> treeview.insert('', '1', 'item2', text = 'Second Item')
'item2'
>>> treeview.insert('', 'end', 'item3', text = 'Third Item')
'item3'
>>> 
>>> logo = PhotoImage(file = 'C:\\Python35\\Python3 - Tech Academy\Tkinter_Exercise Files\\Ch05 - Advanced Widgets\\python_logo.gif').subsample(10,10)
>>> treeview.insert('item2', 'end', 'python', text = 'Python', image = logo)
'python'
>>> 
>>> treeview.config(height = 5)
>>> treeview.move('item2', 'item1', 'end')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    treeview.move('item2', 'item1', 'end')
  File "C:\Python35\lib\tkinter\ttk.py", line 1361, in move
    self.tk.call(self._w, "move", item, parent, index)
_tkinter.TclError: Item item1 not found
>>> treeview.move('item2', 'Item1', 'end')
>>> treeview.item('item1', open = True)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    treeview.item('item1', open = True)
  File "C:\Python35\lib\tkinter\ttk.py", line 1351, in item
    return _val_or_dict(self.tk, kw, self._w, "item", item)
  File "C:\Python35\lib\tkinter\ttk.py", line 297, in _val_or_dict
    res = tk.call(*(args + options))
_tkinter.TclError: Item item1 not found
>>> treeview.item('Item1', open = True)
{}
>>> print(treeview.item('item1', 'open'))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(treeview.item('item1', 'open'))
  File "C:\Python35\lib\tkinter\ttk.py", line 1351, in item
    return _val_or_dict(self.tk, kw, self._w, "item", item)
  File "C:\Python35\lib\tkinter\ttk.py", line 297, in _val_or_dict
    res = tk.call(*(args + options))
_tkinter.TclError: Item item1 not found
>>> print(treeview.item('Item1', 'open'))
1
>>> 
>>> treeview.detach('item3')
>>> treeview.move('item3', 'item2', '0')
>>> treeview.delete('item3')
>>> 
>>> treeview.configure(column = ('version'))
>>> treeview.column('version', width = 50, anchor = 'center')
{}
>>> treeview.column('version', width = 50, anchor = 'center')
{}
>>> treeview.column('#0', width = 150)
{}
>>> treeview.heading('version', text = 'Version')
{}
>>> treeview.set('python', 'version', '3.4')
''
>>> treeview.set('python', 'version', '3.5.1')
''
>>> treeview.item('python', tags = ('software'))
{}
>>> treeview.tag_configure('software', background = 'yellow')
{}
>>> 
>>> def callback(event):
	print(treeview.selection())

	
>>> treeview.bind('<<TreeviewSelect>>', callback)
'2838597892168callback'
>>> ('item2',)
('Item1',)
('Item1',)
('item2',)
('python',)
('item2', 'python')
('Item1', 'item2', 'python')

>>> treeview.config(selectmode = 'browse')
>>> ('Item1',)
('item2',)

>>> treeview.config(selectmode = 'none')
>>> print(treeview.selection_add('python'))
None
>>> ('item2', 'python')

>>> print(treeview.selection_remove('python'))
None
>>> ('item2',)

>>> print(treeview.selection_toggle('python'))
None
>>> ('item2', 'python')
