#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com


# Reading and writing binary files

def main():
    f = open('lines.txt')
    for line in f:
        print(line, end = '')

if __name__ == "__main__": main()
