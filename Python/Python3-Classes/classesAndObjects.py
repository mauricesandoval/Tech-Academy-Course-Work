#!/usr/bin/python3
# This is an exercise file from Python 3 Essential Training on lynda.com


# Understanding classes and objects

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



# call

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    print(donald)
    donald.quack()
    donald.walk()

if __name__ == "__main__": main()
