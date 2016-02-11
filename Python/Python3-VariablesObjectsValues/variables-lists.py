#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com



# Tuple - List type is unmutable
def main():
    x = (1, 2, 3)
    print(type(x),x)

if __name__ == "__main__": main()



# brackets to make mutable
def main():
    x = [1, 2, 3]
    print(type(x),x)

if __name__ == "__main__": main()


# Use square brackets to make mutable
def main():
    x = [1, 2, 3]
    
    print(type(x),x)

if __name__ == "__main__": main()



# Use append
def main():
    x = [1, 2, 3]
    x.append(5)
    print(type(x),x)

if __name__ == "__main__": main()


# Use insert
def main():
    x = [1, 2, 3]
    x.append(5)
    x.insert(2, 7)
    print(type(x),x)

if __name__ == "__main__": main()


# Sequences

# string sequence type
def main():
    x = 'string'
    print(type(x),x[2])

if __name__ == "__main__": main()


# using as iterator
def main():
    x = (1,2,3,4,5)
    for i in x:
        print(i)

if __name__ == "__main__": main()



# using as iterator
def main():
    x = "string"
    for i in x:
        print(i)

if __name__ == "__main__": main()









