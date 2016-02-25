#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com


# Opening Files

def main():
    f = open('lines.txt')
    for line in f:
        print(line, end = '')

if __name__ == "__main__": main()



#### 


def main():
    f = open('lines.txt', 'r') # 'r' = read , other options are 'w'(write) & 'a'(append)
    for line in f.readlines():
        print(line, end = '')

if __name__ == "__main__": main()

