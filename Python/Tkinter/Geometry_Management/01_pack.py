#!/usr/bin/python3

# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# Using the Pack geometry manager
''''
from tkinter import *
from tkinter import ttk        
    
root = Tk()

ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'yellow').pack(fill = BOTH, expand = True)
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'blue').pack(fill = BOTH)
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'green').pack(fill = BOTH, expand = True)


root.mainloop()

'''

'''
# Packing against one side

from tkinter import *
from tkinter import ttk        
    
root = Tk()

ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'yellow').pack(side = LEFT)
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'blue').pack(side = LEFT)
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'green').pack(side = LEFT)
          

root.mainloop()

'''

'''
# Using the anchor property

from tkinter import *
from tkinter import ttk        
    
root = Tk()

ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'yellow').pack(side = LEFT, anchor = 'nw')
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'blue').pack(side = LEFT)
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'green').pack(side = LEFT)


'''
'''
# add padding

from tkinter import *
from tkinter import ttk        
    
root = Tk()

ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'yellow').pack(side = LEFT, anchor = 'nw')
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'blue').pack(side = LEFT, padx = 10, pady = 10)
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'green').pack(side = LEFT)

'''
'''
# add internal padding

from tkinter import *
from tkinter import ttk        
    
root = Tk()

ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'yellow').pack(side = LEFT, anchor = 'nw')
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'blue').pack(side = LEFT)
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'green').pack(side = LEFT, ipadx = 10, ipady = 10)


'''
'''

#configure some property for all widgets of single parent

from tkinter import *
from tkinter import ttk        
    
root = Tk()

ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'yellow').pack(side = LEFT, anchor = 'nw')
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'blue').pack(side = LEFT)
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'green').pack(side = LEFT, ipadx = 10, ipady = 10)

for widget in root.pack_slaves():
    widget.pack_configure(fill = BOTH, expand = True)
    print (widget.pack_info()) 

'''
# if you need to configure or change something about a label in a program later,
# then a variable storing the name to refer to it later will need to be created

# Store the output of a constructor method with the pack method attached to it.

from tkinter import *
from tkinter import ttk        
    
root = Tk()

label = ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'yellow')
label.pack(side = LEFT, anchor = 'nw')
print(label)
      
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'blue').pack(side = LEFT)
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'green').pack(side = LEFT, ipadx = 10, ipady = 10)

for widget in root.pack_slaves():
    widget.pack_configure(fill = BOTH, expand = True)
    print (widget.pack_info())


# label.pack_forget()    'this will get rid of yellow label


