#!/usr/bin/python3

# significance of indentation examples

def main():
    print("This is the syntax.py file.") # Indent shows print statement is
                                         # associated with the main function
if __name__ == "__main__": main()


'''

This will not work due to improper indentation:

def main():
    print("This is the syntax.py file.")
   print("This is another line")
   
if __name__ == "__main__": main()

'''

def main():
    print("This is the syntax.py file.")
print("This is another line") # prints first. Runs before main() is called
   
if __name__ == "__main__": main()



def main():
    print("This is the syntax.py file.") # prints first
    print("This is another line")
   
if __name__ == "__main__": main()


# works when their is just one line of code
def main(): print("This is the syntax.py file.")

if __name__ == "__main__": main()
