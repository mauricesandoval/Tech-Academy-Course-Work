#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com

# using methods



class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == "__main__": main()



# Constructor

class Duck:
    def __init__(self):
        print('constructor')
                
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == "__main__": main()



# Initialize some data

class Duck:
    def __init__(self, value):
        self._v = value
                
    def quack(self):
        print('Quaaack!', self._v)

    def walk(self):
        print('Walks like a duck.', self._v)

def main():
    donald = Duck(47)
    donald.quack()
    donald.walk()

if __name__ == "__main__": main()



# create a diff object with a diff number
# Encapsulation example in OOP

class Duck:
    def __init__(self, value):
        self._v = value
                
    def quack(self):
        print('Quaaack!', self._v)

    def walk(self):
        print('Walks like a duck.', self._v)

def main():
    donald = Duck(47)
    frank = Duck(152)
    donald.quack()
    donald.walk()
    frank.quack()
    frank.walk()

if __name__ == "__main__": main()
