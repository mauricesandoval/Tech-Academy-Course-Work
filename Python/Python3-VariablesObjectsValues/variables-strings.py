#!/usr/bin/python3
# This is an exercise file from Python 3 Essential Training on lynda.com
# Using Strings


def main():
    s = "This is a string!"
    print(s)

if __name__ == "__main__": main()



# adding \n introduces new line in string
def main():
    s = "This is a\nstring!"
    print(s)

if __name__ == "__main__": main()



# adding r to be part of the string i.e raw string
def main():
    s = r"This is a\nstring!"
    print(s)

if __name__ == "__main__": main()



# format and replace variables in the string
def main():
    n = 42
    s = r"This is a {} string!".format(n) # format is a method
    print(s)                              # of the string object
                                          #
if __name__ == "__main__": main()



# another way to define a string
def main():
    n = 42
    s = '''\
this is a string with line
after line of text
'''
    print(s)

if __name__ == "__main__": main()
















