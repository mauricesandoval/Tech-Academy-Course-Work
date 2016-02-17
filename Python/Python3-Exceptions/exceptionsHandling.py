#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com


# Handling exceptions

def main():
    fh = open('lines.txt')
    for line in fh: print(line.strip())

if __name__ == "__main__": main()



# For example purposes: add 'x'to lines.txt to create an error message

def main():
    fh = open('xlines.txt')
    for line in fh: print(line.strip())

if __name__ == "__main__": main()



# trap the exception and use code to do something different

def main():
    try:
        fh = open('xlines.txt')
    except:
        print('could not open the file. come back tomorrow')
    else:
        for line in fh: print(line.strip())

if __name__ == "__main__": main()



# Remove the error to still get actual lines of text

def main():
    try:
        fh = open('lines.txt')
    except:
        print('could not open the file. come back tomorrow')
    else:
        for line in fh: print(line.strip())

if __name__ == "__main__": main()



# Add IOError to get that paticular error

def main():
    try:
        fh = open('xlines.txt')
    except IOError:
        print('could not open the file. come back tomorrow')
    else:
        for line in fh: print(line.strip())

if __name__ == "__main__": main()



# Get the standard Python error message 

def main():
    try:
        fh = open('xlines.txt')
    except IOError as e:
        print('could not open the file:', e)
    else:
        for line in fh: print(line.strip())

if __name__ == "__main__": main()



# Another variation by adding to 'try' clause and removing 'else' 

def main():
    try:
        fh = open('xlines.txt')
        for line in fh: print(line.strip())
    except IOError as e:
        print('could not open the file:', e)

if __name__ == "__main__": main()



# Remove the error to still get actual lines of text

def main():
    try:
        fh = open('lines.txt')
        for line in fh: print(line.strip())
    except IOError as e:
        print('could not open the file:', e)

if __name__ == "__main__": main()

