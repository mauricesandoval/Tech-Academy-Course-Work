#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com


# Applying polymorphism to classes

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



# Add Dog class
#
# These are two seperate and distinct objects with
# two seperate and distinct interfaces
#


class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
        

class Dog:
    def bark(self):
        print ('Woof!')

    def fur(self):
        print('The dog has brown and white fur')


def main():
    donald = Duck()
    donald.quack()
    donald.walk()

    fido = Dog()
    fido.bark()
    fido.fur()
    
if __name__ == "__main__": main()



# To use polymorphically, we need a common interface

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def bark(self):
        print('Duck cannot bark!')

    def fur(self):
        print('The duck had feathers')
        

class Dog:
    def bark(self):
        print ('Woof!')

    def fur(self):
        print('The dog has brown and white fur')

    def walk(self):
        print('Walks like a dog')

    def quack(self):
        print('The dog cannot quack')


def main():
    donald = Duck()
    fido = Dog()

    for o in(donald, fido):
        o.quack()
        o.walk()
        o.bark()
        o.fur()
    
if __name__ == "__main__": main()



# Add more functions
#
# As long as donald implements the interface that is being used in this
# function it will still work
#


class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def bark(self):
        print('Duck cannot bark!')

    def fur(self):
        print('The duck had feathers')
        

class Dog:
    def bark(self):
        print ('Woof!')

    def fur(self):
        print('The dog has brown and white fur')

    def walk(self):
        print('Walks like a dog')

    def quack(self):
        print('The dog cannot quack')


def main():
    donald = Duck()
    fido = Dog()
    in_the_forest(donald)

def in_the_forest(dog):
    dog.bark()
    dog.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()

    
if __name__ == "__main__": main()



# Same as above but call in_the_pond and pass it to fido
#
# As long as fido implements the interface that is being used in this
# function it will still work
#


class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def bark(self):
        print('Duck cannot bark!')

    def fur(self):
        print('The duck had feathers')
        

class Dog:
    def bark(self):
        print ('Woof!')

    def fur(self):
        print('The dog has brown and white fur')

    def walk(self):
        print('Walks like a dog')

    def quack(self):
        print('The dog cannot quack')


def main():
    donald = Duck()
    fido = Dog()
    in_the_forest(donald)
    in_the_pond(fido)       # called and added here

def in_the_forest(dog):
    dog.bark()
    dog.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()

    
if __name__ == "__main__": main()


