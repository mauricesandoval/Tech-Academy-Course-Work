#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com

# Creating a sequence with a generator

def main():
    print("This is the functions.py file.")
    for i in range(25):
        print(i, end = ' ')

if __name__ == "__main__": main()




# create a 'yield' generator

def main():
    print("This is the functions.py file.")
    for i in inclusive_range(0, 25, 1):
        print(i, end = ' ')

def inclusive_range(start, stop, step):
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == "__main__": main()




# use all techniques learned from function drills so far

# this first example will result in error 

def main():
    print("This is the functions.py file.")
    for i in inclusive_range(25):
        print(i, end = ' ')

def inclusive_range(start = 0, stop, step = 1):  # this is not allowable
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == "__main__": main()




# fix above error with a tuple

def main():
    print("This is the functions.py file.")
    for i in inclusive_range(25):
        print(i, end = ' ')

def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError('requires at least one argument')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step)
    else: raise TypeError('inclusive_range expected at most 3 arguments, got {}'.format(numargs))
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == "__main__": main()




# add '5' to range

def main():
    print("This is the functions.py file.")
    for i in inclusive_range(5, 25):
        print(i, end = ' ')

def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError('requires at least one argument')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step)
    else: raise TypeError('inclusive_range expected at most 3 arguments, got {}'.format(numargs))
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == "__main__": main()




# add step by '3'to range

def main():
    print("This is the functions.py file.")
    for i in inclusive_range(5, 25, 3):
        print(i, end = ' ')

def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError('requires at least one argument')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError('inclusive_range expected at most 3 arguments, got {}'.format(numargs))
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == "__main__": main()




# add step by '42' to range to trigger error

def main():
    print("This is the functions.py file.")
    for i in inclusive_range(5, 25, 3, 42):
        print(i, end = ' ')

def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError('requires at least one argument')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError('inclusive_range expected at most 3 arguments, got {}'.format(numargs))
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == "__main__": main()




# remove values from range to trigger the other error

def main():
    print("This is the functions.py file.")
    for i in inclusive_range():
        print(i, end = ' ')

def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError('requires at least one argument')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError('inclusive_range expected at most 3 arguments, got {}'.format(numargs))
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == "__main__": main()













