#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com


# Reading and writing text files

def main():
    f = open('lines.txt')
    for line in f:
        print(line, end = '')

if __name__ == "__main__": main()



# Use print and file parameter for print

def main():
    infile = open('lines.txt', 'r')
    outfile = open('new.text', 'w')
    for line in infile:
        print(line, file = outfile, end = '')
    print('Done')

if __name__ == "__main__": main()



# Use bigfile.txt
# Set up buffered mode

def main():
    buffersize = 50000
    infile = open('bigfile.txt', 'r')
    outfile = open('new.text', 'w')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end = '')
        buffer = infile.read(buffersize)
    print()
    print('Done')

if __name__ == "__main__": main()



