#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com


# Understanding Inheritance

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



# Add class Animal

class Animal:
    def talk(self): print('I have something to say!')
    def walk(self): print('Hey! I''m walkin'' here!')
    def clothes(self): print('I have nice clothes')


class Duck(Animal):
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    
if __name__ == "__main__": main()



# Add donald.clothes()

class Animal:
    def talk(self): print('I have something to say!')
    def walk(self): print('Hey! I''m walkin'' here!')
    def clothes(self): print('I have nice clothes')


class Duck(Animal):
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.clothes()
    
if __name__ == "__main__": main()



# Access Parent class

class Animal:
    def talk(self): print('I have something to say!')
    def walk(self): print('Hey! I''m walkin'' here!')
    def clothes(self): print('I have nice clothes')


class Duck(Animal):
    def quack(self):
        print('Quaaack!')

    def walk(self):
        super().walk()  # Access parent class here
        print('Walks like a duck.')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.clothes()
    
if __name__ == "__main__": main()



# Add another animal

class Animal:
    def talk(self): print('I have something to say!')
    def walk(self): print('Hey! I''m walkin'' here!')
    def clothes(self): print('I have nice clothes')


class Duck(Animal):
    def quack(self):
        print('Quaaack!')

    def walk(self):
        super().walk()  # Access parent class here
        print('Walks like a duck.')

class Dog(Animal):
    pass

def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.clothes()

    fido = Dog()
    fido.walk()
    
if __name__ == "__main__": main()


# 

class Animal:
    def talk(self): print('I have something to say!')
    def walk(self): print('Hey! I''m walkin'' here!')
    def clothes(self): print('I have nice clothes')


class Duck(Animal):
    def quack(self):
        print('Quaaack!')

    def walk(self):
        super().walk()  # Access parent class here
        print('Walks like a duck.')

class Dog(Animal):
    def clothes(self):  
        print('I have brown and white fur')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.clothes()

    fido = Dog()
    fido.walk()
    fido.clothes()
    
if __name__ == "__main__": main()

