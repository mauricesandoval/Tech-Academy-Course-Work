#!/usr/bin/python3


def main():
    a, b = 0, 1
    if a < b:
        print("a is less than b")

    
if __name__ == "__main__": main()



# change to 0 and add else
def main():
    a, b = 1, 1
    if a < b:
        print("a is less than b")
    else:
        print("a is not less than b")
    
if __name__ == "__main__": main()



# change to 2 and add elif
def main():
    a, b = 2, 1
    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is equal to b")
    
if __name__ == "__main__": main()



# conditonal expression (or conditional value) example
def main():
    a, b = 0, 1
    s = "Less than" if a < b else "not less than"
    print(s)
   
if __name__ == "__main__": main()



# conditonal expression (or conditional value) example 2 
def main():
    a, b = 1, 1
    s = "Less than" if a < b else "not less than"
    print(s)
   
if __name__ == "__main__": main()





