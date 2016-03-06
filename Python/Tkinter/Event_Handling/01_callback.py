#!/usr/bin/python3

# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# Configuring command callbacks

'''
from tkinter import *
from tkinter import ttk        
    
root = Tk()

def callback():
    print('In the callback')

ttk.Button(root, text = 'Click Me!', command = callback).pack()


root.mainloop()

'''
'''


from tkinter import *
from tkinter import ttk

root = Tk()

def callback(number):
    print(number)

ttk.Button(root, text = 'Click Me 1', command = callback(1)).pack()
ttk.Button(root, text = 'Click Me 2', command = callback(2)).pack()
ttk.Button(root, text = 'Click Me 3', command = callback(3)).pack()

root.mainloop()
'''


from tkinter import *
from tkinter import ttk        

def callback(number):
    print(number)
    
root = Tk()

ttk.Button(root, text = 'Click Me 1', command = lambda: callback(1)).pack()
ttk.Button(root, text = 'Click Me 2', command = lambda: callback(2)).pack()
ttk.Button(root, text = 'Click Me 3', command = lambda: callback(3)).pack()

root.mainloop()


