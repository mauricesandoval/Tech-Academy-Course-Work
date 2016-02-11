#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com
# Using Numbers

def main():
    num = 42
    print(num)

if __name__ == "__main__": main()



#Add type and value - integer

def main():
    num = 42
    print(type(num), num)

if __name__ == "__main__": main()



#Add type and value - non integer

def main():
    num = 42 / 9
    print(type(num), num)

if __name__ == "__main__": main()



#Add type and value - non integer - add extra slash for integer division

def main():
    num = 42 // 9
    print(type(num), num)

if __name__ == "__main__": main()



#Add type and value - non integer - round up - round()

def main():
    num = round(42 / 9)
    print(type(num), num)

if __name__ == "__main__": main()



# define how many digits rounded to
def main():
    num = round(42 / 9, 2)
    print(type(num), num)

if __name__ == "__main__": main()




# get remainder by using % (modulo)
def main():
    num = round(42 % 9)
    print(type(num), num)

if __name__ == "__main__": main()



# to make sure floating point number read as integer 
def main():
    num = int(42.9)
    print(type(num), num)

if __name__ == "__main__": main()



# to make sure integerread as floating point number
def main():
    num = float(42)
    print(type(num), num)

if __name__ == "__main__": main()









