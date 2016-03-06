#!/usr/bin/python3

# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# Binding to virtual events

'''

from tkinter import *
from tkinter import ttk        
    
root = Tk()

entry = ttk.Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))


root.mainloop()

'''

'''

from tkinter import *
from tkinter import ttk        
    
root = Tk()

entry = ttk.Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))

entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
entry.bind('<<OddNumber>>', lambda e: print('Odd Number!'))

root.mainloop()

'''

'''
from tkinter import *
from tkinter import ttk        
    
root = Tk()

entry = ttk.Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))

entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
entry.bind('<<OddNumber>>', lambda e: print('Odd Number!'))

print(entry.event_info('<<OddNumber>>'))



root.mainloop()

'''

'''

from tkinter import *
from tkinter import ttk        
    
root = Tk()

entry = ttk.Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))

entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
entry.bind('<<OddNumber>>', lambda e: print('Odd Number!'))

print(entry.event_info('<<OddNumber>>'))

entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')


root.mainloop()

'''


from tkinter import *
from tkinter import ttk        
    
root = Tk()

entry = ttk.Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))

entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
entry.bind('<<OddNumber>>', lambda e: print('Odd Number!'))

print(entry.event_info('<<OddNumber>>'))

entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')

entry.event_delete('<<OddNumber>>')


root.mainloop()

