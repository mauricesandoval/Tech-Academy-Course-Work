#!/usr/bin/python3
 
# This is an exercise file from Python 3 Essential Training on lynda.com

# Controlling loop flow with break, continue, and else



# Simple Loop

def main():
    s = 'this is a string'
    for c in s:
        print(c, end='')

if __name__ == "__main__": main()



# Use continue to shortcut the loop - skip all 's'

def main():
    s = 'this is a string'
    for c in s:
        if c == 's': continue
        print(c, end='')

if __name__ == "__main__": main()



# Use break to to look for the first 's'

def main():
    s = 'this is a string'
    for c in s:
        if c == 's': break
        print(c, end='')

if __name__ == "__main__": main()



# Use else 

def main():
    s = 'this is a string'
    for c in s:
        print(c, end='')
    else:
        print('else')

if __name__ == "__main__": main()



# Use While loop 

def main():
    s = 'this is a string'
    i = 0
    while(i < len(s)):
        print(s,[i], end='')
        i += 1
    else:
        print('else')

if __name__ == "__main__": main()









