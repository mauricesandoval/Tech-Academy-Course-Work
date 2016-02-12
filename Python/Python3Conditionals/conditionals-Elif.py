#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com

# Conditonals - Elif


def main():
    v = 'one'
    if v == 'one':
        print('v is one')
    elif v == 'two':
        print('v is two')
    elif v == 'three':
        print('v is three')
    
if __name__ == "__main__": main()



# change value, add default via else clause

def main():
    v = 'seven'
    if v == 'one':
        print('v is one')
    elif v == 'two':
        print('v is two')
    elif v == 'three':
        print('v is three')
    else:
        print('v is some other thing')

if __name__ == "__main__": main()
