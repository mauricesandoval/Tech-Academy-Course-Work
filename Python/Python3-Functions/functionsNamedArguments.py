#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com

# Passing named arguments to a function



# Using named function arguments

def main():
    testfunc()

def testfunc():
    print('This is a test function')

if __name__ == "__main__": main()



# Using named function arguments

def main():
    testfunc(one = 1, two = 2, four = 42)

def testfunc(**kwargs):
    print('This is a test function', kwargs['one'], kwargs['two'], kwargs['four'])

if __name__ == "__main__": main()



# keyword arguments combined with positional arguments

def main():
    testfunc(5, 6, 7, 8, 9, 10, one = 1, two = 2, four = 42)

def testfunc(this, that, other, *args, **kwargs):
    print('This is a test function',
          this, that, other, args,
          kwargs['one'], kwargs['two'], kwargs['four'])

if __name__ == "__main__": main()



# keyword arguments

def main():
    testfunc(5, 6, 7, 8, 9, 10, one = 1, two = 2, four = 42)

def testfunc(this, that, other, *args, **kwargs):
    for k in kwargs: print(k, kwargs[k])

if __name__ == "__main__": main()



# keyword arguments - change to '2' to 'seventeen'

def main():
    testfunc(5, 6, 7, 8, 9, 10, one = 1, seventeen = 2, four = 42)

def testfunc(this, that, other, *args, **kwargs):
    for k in kwargs: print(k, kwargs[k])

if __name__ == "__main__": main()



# use print(n) for the order that they were passes

def main():
    testfunc(5, 6, 7, 8, 9, 10, one = 1, seventeen = 2, four = 42)

def testfunc(this, that, other, *args, **kwargs):
    for n in args: print(n)

if __name__ == "__main__": main()









