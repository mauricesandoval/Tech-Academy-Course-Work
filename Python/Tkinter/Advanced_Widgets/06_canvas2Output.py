Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> 
>>> canvas = Canvas(root)
>>> canvas.pack()
>>> canvas.config(width = 640, height = 480)
>>> 
>>> rect = canvas.create_rectangle(160, 120, 480, 360)
>>> canvas.itemconfigure(rect, fill = 'yellow')
>>> oval = canvas.create_oval(160, 120, 480, 360)
>>> arc = canvas.create_arc(160, 1, 480, 240)
>>> canvas.itemconfigure(arc, start = 0, extent = 180, fill = 'green')
>>> poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill = 'blue')
>>> text = canvas.create_text(320, 240, text = 'Python', font = ('Courier', 32, 'bold'))
>>> 
>>> logo = PhotoImage(file = 'C:\\Python35\Python3 - Tech Academy\\Tkinter_Exercise Files\\Ch05 - Advanced Widgets \\python_logo.gif')
>>> image = canvas.create_image(320, 240, image = logo)
>>> 
>>> 
>>> canvas.lift(text)
>>> canvas.lower(image)
>>> canvas.lower(image, text)
>>> 
>>> button = Button(canvas, text = 'Click Me')
>>> canvas.create_window(320, 60, window = button)
7
>>> canvas.itemconfigure(rect, tags = ('shape'))
>>> canvas.itemconfigure(oval, tags = ('shape', 'round'))
>>> canvas.itemconfigure('shape', fill = 'grey')
>>> print(canvas.gettags(oval))
('shape', 'round')
>>> 
