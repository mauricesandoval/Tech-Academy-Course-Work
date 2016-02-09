#!/usr/bin/python3

# Using functions
# define a function
# call and use that function
# use arguments to call and use the function


def main():
    func()
def func():
    for i in range(10):
        print(i, end=' ')
    print()
    
if __name__ == "__main__": main()

# You can call the function as many times as you like
def main():
    func()
    func()
    func()
    
def func():
    for i in range(10):
        print(i, end=' ')
    print()
    
if __name__ == "__main__": main()


# Enter an argument
def main():
    func(1)
    func(3)
    func(5)
    
def func(a):
    for i in range(a, 10):
        print(i, end=' ')
    print()
    
if __name__ == "__main__": main()


# Give the argument a default value
def main():
    func(1)
    func()
    func(5)
    
def func(a=7):
    for i in range(a, 10):
        print(i, end=' ')
    print()
    
if __name__ == "__main__": main()

