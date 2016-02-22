#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com


# Using generators

def main():
    o = range(25)
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()




# Range can take three possible arguments (start, stop, step)
# but only requires one (as shown above)


def main():
    o = range(0, 25, 1)
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()




# change arguments

def main():
    o = range(5, 25, 2)
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()




# create a range object - 1st step

class inclusive_range:
    def __init__(self):    # constructor
        pass

    def __iter__(self):    # generator function
        pass


def main():
    o = range(5, 25, 2)
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()




# create a range object - 2nd step

class inclusive_range:
    def __init__(self, *args):        # constructor
        numargs = len(args)
        if < 1: raise TypeError('requires at least one argument')
        elif numargs == 1:
            pass
        elif numargs == 2:
            pass
        elif numargs == 3:
            pass
        else: raise TypeError('expected at most 3 arguments, got {}'.format(numargs))

    def __iter__(self):               # generator function
        pass


def main():
    o = range(25)
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()




# create a range object - 3rd step
# Fill in conditions

class inclusive_range:
    def __init__(self, *args):        # constructor
        numargs = len(args)
        if numargs < 1: raise TypeError('requires at least one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('expected at most 3 arguments, got {}'.format(numargs))

    def __iter__(self):               # generator function
        i = self.start
        while i <= self.stop:
            yield i                   # Yield is what makes this a generator
            i += self.step


def main():
    o = inclusive_range(25)           # add inclusive
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()




# Test the constructor - change start point to 5

class inclusive_range:
    def __init__(self, *args):        # constructor
        numargs = len(args)
        if numargs < 1: raise TypeError('requires at least one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('expected at most 3 arguments, got {}'.format(numargs))

    def __iter__(self):               # generator function
        i = self.start
        while i <= self.stop:
            yield i                   # Yield is what makes this a generator
            i += self.step


def main():
    o = inclusive_range(5, 25)        # add 5 as start point
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()




# Test the constructor - change step point to 2

class inclusive_range:
    def __init__(self, *args):        # constructor
        numargs = len(args)
        if numargs < 1: raise TypeError('requires at least one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('expected at most 3 arguments, got {}'.format(numargs))

    def __iter__(self):               # generator function
        i = self.start
        while i <= self.stop:
            yield i                   # Yield is what makes this a generator
            i += self.step


def main():
    o = inclusive_range(5, 25,2)      # add 2 as step point
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()




# Test for Error conditions - remove arguments

class inclusive_range:
    def __init__(self, *args):        # constructor
        numargs = len(args)
        if numargs < 1: raise TypeError('requires at least one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('expected at most 3 arguments, got {}'.format(numargs))

    def __iter__(self):               # generator function
        i = self.start
        while i <= self.stop:
            yield i                   # Yield is what makes this a generator
            i += self.step


def main():
    o = inclusive_range()      # remove arguments - test for error condition
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()




# Test for Error conditions - add four arguments

class inclusive_range:
    def __init__(self, *args):        # constructor
        numargs = len(args)
        if numargs < 1: raise TypeError('requires at least one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('expected at most 3 arguments, got {}'.format(numargs))

    def __iter__(self):               # generator function
        i = self.start
        while i <= self.stop:
            yield i                   # Yield is what makes this a generator
            i += self.step


def main():
    o = inclusive_range(1, 25, 3, 14) # add 4 arguments - test for error condition
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()




# Final script
# Successful example of duplicating the range generator function
# This is inclusive

class inclusive_range:
    def __init__(self, *args):        # constructor
        numargs = len(args)
        if numargs < 1: raise TypeError('requires at least one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('expected at most 3 arguments, got {}'.format(numargs))

    def __iter__(self):               # generator function
        i = self.start
        while i <= self.stop:
            yield i                   # Yield is what makes this a generator
            i += self.step


def main():
    o = inclusive_range(25) 
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()

