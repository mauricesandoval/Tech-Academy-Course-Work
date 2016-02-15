#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com

# Replacing with Regular Expressions


import re

def main():
    fh = open('raven.txt')
    for line in fh:
        if re.search('(Len|Neverm)ore', line):
            print(line, end='')

if __name__ == "__main__": main()



# Search and Replace

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        print(re.sub('(Len|Neverm)ore', '###', line), end= '')
          
if __name__ == "__main__": main()



# Print location(lines) where string is found only

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(line.replace(match.group(), '###'), end='')
          
if __name__ == "__main__": main()














