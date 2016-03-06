#!/usr/bin/python3

# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# Organizing widgets with frames

from tkinter import *
from tkinter import ttk        
    
root = Tk()

frame = ttk.Frame(root)
frame.pack()
frame.config(height = 100, width = 200)
frame.config(relief = RIDGE)
ttk.Button(frame, text = 'Click Me').grid()
frame.config(padding = (30, 15))
ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()

root.mainloop()
