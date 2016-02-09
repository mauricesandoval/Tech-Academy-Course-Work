#!/usr/bin/python3
#creating and using objects

# define a class i.e a definition used when creating an object

class Egg:
    def __init__(self, kind = "fried"):   # __init__ is a constructor which
        self.kind = kind                 # is a method/function in a class

    def whatKind(self):
        return self.kind
        
def main():
    fried = Egg()
    scrambled = Egg('scrambled')
    print(fried.whatKind())
    
if __name__ == "__main__": main()




# change to scrambled

class Egg:
    def __init__(self, kind = "fried"):   # __init__ is a constructor which
        self.kind = kind                 # is a method/function in a class

    def whatKind(self):
        return self.kind
        
def main():
    fried = Egg()
    scrambled = Egg('scrambled')
    print(scrambled.whatKind())
    
if __name__ == "__main__": main()
