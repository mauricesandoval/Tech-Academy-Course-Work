#!/usr/bin/python3
# 
# This is an exercise file from Python 3 Essential Training on lynda.com
#
# For Loop - Enumerating Iterators

# For Loop

def main():
    fh = open('lines.txt')
    for line in fh.readlines():
        print(line)

if __name__ == "__main__": main()



# add enumerator function

def main():
    fh = open('lines.txt')
    for index, line in enumerate(fh.readlines()):
        print(index, line, end = '')

if __name__ == "__main__": main()



# iterate over a string

def main():
    s = 'this is a string'
    for i, c in enumerate(s):
        print(i, c)

if __name__ == "__main__": main()



# Get indexes and an inerator with a for loop

# Find out which charachter is the letter 's'

def main():
    s = 'this is a string'
    for i, c in enumerate(s):
        if c == 's': print('index {} is an s'.format (i))

if __name__ == "__main__": main()


