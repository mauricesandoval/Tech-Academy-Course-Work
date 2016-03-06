#!/usr/bin/python3

# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# Basic template of a common structure for coding GUI applications

from tkinter import *
from tkinter import ttk
                                   ## Feedback form is impplemeted as a class 
class Feedback:                    ## which you will need to complete by filling            
                                   ## in the INIT method

    def __init__(self, master):     
        pass                       ## INIT constructor method takes a parameter called
                                   ## master, which will be the top-level TK widget
                                   ## that you build feedback form

            
def main():                        # The main function creates a new top level TK window
                                   # which it passs to the feedback constructor to be used
    root = Tk()                    # as the master widget
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()  # conditional statement that will only call that main fuction
                                   # if this Python file is run as the main script


# By running the code this way, we can run our feedback script on its own and will create a feedback
# form inside of the new TK window
 
