#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com


# Handling exceptions



def main():
    fh = open('lines.txt')
    for line in fh: print(line.strip())

if __name__ == "__main__": main()
