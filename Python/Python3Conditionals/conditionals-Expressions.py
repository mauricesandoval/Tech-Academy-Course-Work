#!/usr/bin/python3
# This is an exercise file from Python 3 Essential Training on lynda.com

# Conditional Expressions


# Typical if-else statement

def main():
    a, b = 0, 1
    if a < b:
        v = 'this is true'
    else:
        v = 'this is not true'
    print(v)

if __name__ == "__main__": main()


#Better method using Conditional Expression

def main():
    a, b = 0, 1
    v = 'this is true' if a < b else 'this is not true'
    print(v)

if __name__ == "__main__": main()
