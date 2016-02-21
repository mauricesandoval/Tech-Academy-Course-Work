#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com


# Using lists of arguments

def main():
    testfunc()

def testfunc():
    print('This is a test function')

if __name__ == "__main__": main()



# Give it an arbitrary list of arguments

def main():
    testfunc(1, 2, 3, 42, 43, 45, 46)

def testfunc(this, that, other, *args):
    print(this, that, other)

if __name__ == "__main__": main()



 #use *args in print line for tuple

def main():
    testfunc(1, 2, 3, 42, 43, 45, 46)

def testfunc(this, that, other, *args):
    print(this, that, other, args)

if __name__ == "__main__": main()



# use as an interator
# prints arbitrary arguments after the names arguments

def main():
    testfunc(1, 2, 3, 42, 43, 45, 46)

def testfunc(this, that, other, *args):
    print(this, that, other)
    for n in args: print(n, end=' ')

if __name__ == "__main__": main()




