#!/usr/bin/python3
# This is an exercise file from Python 3 Essential Training on lynda.com

# Creating Associative List with Dictionaries


def main():
    d = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5}
    print(d)

if __name__ == "__main__": main()



# step through keys and print values
def main():
    d = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5}
    for k in d:
        print(k, d[k])

if __name__ == "__main__": main()



# make a sorted order
def main():
    d = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5}
    for k in sorted(d.keys()):
        print(k, d[k])

if __name__ == "__main__": main()



#use better syntax - key word arguments
def main():
    d = dict(one = 1, two = 2, three = 3, four = 4, five = 'five')
    for k in sorted(d.keys()):
        print(k, d[k])

if __name__ == "__main__": main()



# add a new value to the dictionary
def main():
    d = dict(
        one = 1, two = 2, three = 3, four = 4, five = 'five'
    )
    d['seven'] = 7
    for k in sorted(d.keys()):
        print(k, d[k])
    
if __name__ == "__main__": main()









