#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com


# Using object data in classes

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



# Add a constructor

class Duck:
    def __init__(self, color = 'white'):
        self._color = color
        
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    donald._color = 'blue'
    print(donald._color)

if __name__ == "__main__": main()



# Add a constructor - this variation prints white first

class Duck:
    def __init__(self, color = 'white'):
        self._color = color
        
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    print(donald._color)
    donald._color = 'blue'
    print(donald._color)

if __name__ == "__main__": main()



# Accessor Method

class Duck:
    def __init__(self, color = 'white'):
        self._color = color
        
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
        
    def set_color(self, color):
        self._color = color
    
    def get_color(self):
        return self._color 

def main():
    donald = Duck()
    print(donald.get_color())
    donald.set_color('blue')
    print(donald.get_color())   

if __name__ == "__main__": main()



# Use keyword argument

class Duck:
    def __init__(self, **kwargs):
        self._color = kwargs.get('color', 'white')
        
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
        
    def set_color(self, color):
        self._color = color
    
    def get_color(self):
        return self._color 

def main():
    donald = Duck(color = 'blue')
     
    print(donald.get_color())   

if __name__ == "__main__": main()



# same as above without passing the argument

class Duck:
    def __init__(self, **kwargs):
        self._color = kwargs.get('color', 'white')
        
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
        
    def set_color(self, color):
        self._color = color
    
    def get_color(self):
        return self._color 

def main():
    donald = Duck() # removed here - no argument passed
    print(donald.get_color())   

if __name__ == "__main__": main()



# use a dictionary

class Duck:
    def __init__(self, **kwargs):
        self.variables = kwargs  # changed here
        
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
        
    def set_color(self, color):
        self.variables['color'] = color
    
    def get_color(self):
        return self.variables.get('color', None) 

def main():
    donald = Duck(feet = 2)  #Added here
    print(donald.get_color())   

if __name__ == "__main__": main()



# we're really getting into some power here

class Duck:
    def __init__(self, **kwargs):
        self.variables = kwargs  
        
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
        
    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)

def main():
    donald = Duck(feet = 2)  
    print(donald.get_variable('feet'))   

if __name__ == "__main__": main()



# this allows acalability, even after Donald is created, we can still set color

class Duck:
    def __init__(self, **kwargs):
        self.variables = kwargs  
        
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
        
    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)

def main():
    donald = Duck(feet = 2)
    donald.set_variable('color', 'blue')
    print(donald.get_variable('feet'))   
    print(donald.get_variable('color'))
    
if __name__ == "__main__": main()

