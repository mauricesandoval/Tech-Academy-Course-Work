#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com


# Defining Functions

def main():
    testfunc()

def testfunc():
    print('This is a test function')

if __name__ == "__main__": main()



# Removing 'def main()' causes error because 'testfunc()' is not defined

testfunc()

def testfunc():
    print('This is a test function')

if __name__ == "__main__": main()



# Error results because of no content

def main():
    testfunc()

def testfunc():
    

if __name__ == "__main__": main()



# Add 'pass' to solve Error results because of no content - this does nothing

def main():
    testfunc()

def testfunc():
    pass

if __name__ == "__main__": main()



# Pass an argument to the function

def main():
    testfunc(42)

def testfunc(number):
    print('This is a test function', number)

if __name__ == "__main__": main()



# add more numbers - if they are defined, then they must be passed

def main():
    testfunc(42,43,75)

def testfunc(number, another, onemore):
    print('This is a test function', number, another, onemore)

if __name__ == "__main__": main()



# if they are defined and not passed - this results in error

def main():
    testfunc(42)

def testfunc(number, another, onemore):
    print('This is a test function', number, another, onemore)

if __name__ == "__main__": main()



# default values given to optional arguments
# assign the values in the function position

def main():
    testfunc(42)

def testfunc(number, another = 43, onemore =75):
    print('This is a test function', number, another, onemore)

if __name__ == "__main__": main()



# default values will not be used in this instance for the secoond case


def main():
    testfunc(42, 16)

def testfunc(number, another = 43, onemore =75):
    print('This is a test function', number, another, onemore)

if __name__ == "__main__": main()



# using the value 'None'

def main():
    testfunc(42)

def testfunc(number, another = None, onemore =75):
    print('This is a test function', number, another, onemore)

if __name__ == "__main__": main()



# Test for 'None'

def main():
    testfunc(42)

def testfunc(number, another = None, onemore =75):
    if another is None:
        another = 112  # assigning here 
    print('This is a test function', number, another, onemore)

if __name__ == "__main__": main()



# adding 16 to testfunc()

def main():
    testfunc(42, 16)

def testfunc(number, another = None, onemore =75):
    if another is None:
        another = 112  # assigning here 
    print('This is a test function', number, another, onemore)

if __name__ == "__main__": main()







