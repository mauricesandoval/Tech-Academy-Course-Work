#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com


# Reading and writing binary files

def main():
    f = open('lines.txt')
    for line in f:
        print(line, end = '')

if __name__ == "__main__": main()



# Results in Error due to Python trying to decode text in jPeg file

def main():
    f = open('olives.jpg')
    for line in f:
        print(line, end = '')

if __name__ == "__main__": main()



# Use rb to open. 'rb' = read binary
# Output is still not optimal

def main():
    f = open('olives.jpg', 'rb')
    for line in f:
        print(line, end = '')
        break

if __name__ == "__main__": main()



#### 

def main():
    buffersize = 50000
    infile = open('olives.jpg', 'rb')
    outfile = open('new.jpg', 'wb')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end = '')
        buffer = infile.read(buffersize)
    print()
    print('Done.')
    
if __name__ == "__main__": main()



