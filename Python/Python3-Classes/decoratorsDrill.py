#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com


# Using decorators

class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

def main():
    donald = Duck(color = 'blue')
    print(donald.get_property('color'))

if __name__ == "__main__": main()



# Using decorators - create an  accessor method for variables
# create special accessors for color

class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

    @property           # this decorator function is what makes accessor
    def color(self):
        return self.properties.get('color', None)

    @color.setter
    def color(self, c):
        self.properties['color'] = c

    @color.deleter
    def color(self):
        del self.properties['coloe']

def main():
    donald = Duck()         # remove: (color = 'blue')
    donald.color = 'blue'   # add color here 
    print(donald.get_property('color'))

if __name__ == "__main__": main()



# Using decorators - change print line in def main

class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

    @property           # this decorator function is what makes accessor
    def color(self):
        return self.properties.get('color', None)

    @color.setter
    def color(self, c):
        self.properties['color'] = c

    @color.deleter
    def color(self):
        del self.properties['coloe']

def main():
    donald = Duck()         
    donald.color = 'blue'    
    print(donald.color)     # remove:(donald.get_property('color'))

if __name__ == "__main__": main()
