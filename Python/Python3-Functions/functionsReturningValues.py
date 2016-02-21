#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com


# Returning Values from functions


def main():
    testfunc()

def testfunc():
    print('This is a test function')

if __name__ == "__main__": main()



# use return

def main():
    print(testfunc())

def testfunc():
    return 'This is a test function'

if __name__ == "__main__": main()



# return a number
def main():
    print(testfunc())

def testfunc():
    return 42

if __name__ == "__main__": main()



# return an object

def main():
    print(testfunc())

def testfunc():
    return range(25)

if __name__ == "__main__": main()



# return an object - in this case a range object

def main():
    print(testfunc())

def testfunc():
    return range(25)

if __name__ == "__main__": main()



# range object now isable as an interator

def main():
    for n in testfunc(): print(n, end=' ')

def testfunc():
    return range(25)

if __name__ == "__main__": main()







