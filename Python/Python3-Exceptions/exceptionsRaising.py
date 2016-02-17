#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com


# Raising exceptions


def main():
    fh = open('lines.txt')
    for line in fh: print(line.strip())

if __name__ == "__main__": main()



# Write a finction to return that will open a file and return lines of text

def main():
    for line in readfile('lines.txt'): print(line.strip())
    
def readfile(filename):
    fh = open(filename)
    return fh.readlines()
             
if __name__ == "__main__": main()



# Create an error - add 'x' to files.txt

def main():
    for line in readfile('xlines.txt'): print(line.strip())
    
def readfile(filename):
    fh = open(filename)
    return fh.readlines()
             
if __name__ == "__main__": main()



# Handle the error created above

def main():
    try:
        for line in readfile('xlines.txt'): print(line.strip())
    except IOError as e:
        print('cannot read file:', e)
        
def readfile(filename):
    fh = open(filename)
    return fh.readlines()
             
if __name__ == "__main__": main()



# Raising a conditon for another error

def main():
    try:
        for line in readfile('xlines.doc'): print(line.strip())
    except IOError as e:
        print('cannot read file:', e)
        
def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError('Filename must end with .txt')
             
if __name__ == "__main__": main()



# Handle above error with sperate 'except' statement

def main():
    try:
        for line in readfile('xlines.doc'): print(line.strip())
    except IOError as e:
        print('cannot read file:', e)
    except ValueError as e:
        print('bad filenname', e)
        
def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError('Filename must end with .txt')
             
if __name__ == "__main__": main()



