#!/usr/bin/python3

# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# Building a hierarchical treeview

from tkinter import *
from tkinter import ttk        
    
root = Tk()

treeview = ttk.Treeview(root)
treeview.pack()
treeview.insert('', '0', 'item1', text = 'First Item')
treeview.insert('', '1', 'item2', text = 'Second Item')
treeview.insert('', 'end', 'item3', text = 'Third Item')

logo = PhotoImage(file = 'C:\\Users\\barron\\Dropbox\\Lynda Courses\\Python GUI Development with Tkinter\\Exercise Files - Current\\03 Widget Classes\\python_logo.gif').subsample(10,10)
treeview.insert('item2', 'end', 'python', text = 'Python', image = logo)

treeview.config(height = 5)
treeview.move('item2', 'item1', 'end')
treeview.item('item1', open = True)
treeview.item('item2', open = True)
print(treeview.item('item1', 'open'))

treeview.detach('item3')
treeview.move('item3', 'item2', '0')
treeview.delete('item3')

