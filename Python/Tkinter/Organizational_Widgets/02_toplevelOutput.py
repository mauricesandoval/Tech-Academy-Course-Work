Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> root = Tk()
>>> 
>>> window = Toplevel(root)
>>> window.title('New Window')
''
>>> window.lower()
>>> window.lift(root)
>>> 
>>> window.state('zoomed')
''
>>> window.state('withdrawn')
''
>>> window.state('iconic')
''
>>> window.state('normal')
''
>>> print(window.state())
zoomed
>>> window.state('normal')
''
>>> 
>>> window.iconify()
''
>>> window.deiconify()
''
>>> window.geometry('640x480+50+100')
''
>>> print(window.geometry())
640x480+50+100
>>> window.resizable(False, False)
''
>>> window.maxsize(640, 480)
>>> window.minsize(200, 200)
>>> window.resizable(True, True)
''
>>> root.destroy()
