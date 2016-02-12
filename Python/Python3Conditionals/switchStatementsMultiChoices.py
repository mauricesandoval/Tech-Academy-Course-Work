#!/usr/bin/python3
# switch.py
# This is an exercise file from Python 3 Essential Training on lynda.com
#
# Conditionals - Strategies for multiple choices


def main():
    choices = dict(
            one = 'first',
            two = 'second',
            three = 'third',
            four = 'fourth',
            five = 'fifth'
        )
    v = 'one'
    print(choices[v])

if __name__ == "__main__": main()



#use get method of the dictionary object to use a default result

def main():
    choices = dict(
            one = 'first',
            two = 'second',
            three = 'third',
            four = 'fourth',
            five = 'fifth'
        )
    v = 'seven'
    print(choices.get(v, 'other'))

if __name__ == "__main__": main()
