#!/usr/bin/python3

# This is an exercise file from Python 3 Essential Training on lynda.com

'''
#Using Standard library modules

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))

if __name__ == "__main__": main()



#### Get system platform

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

if __name__ == "__main__": main()



#### use import os

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    import os
    print(os.name)

if __name__ == "__main__": main()


#### get variables from the environment

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    import os
    print(os.name)
    print(os.getenv('PATH'))

if __name__ == "__main__": main()



#### get current working directory

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    import os
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())

if __name__ == "__main__": main()


#### urandom function (give string of random bytes)

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    import os
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.urandom(25))

if __name__ == "__main__": main()



#### urllib module

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    import urllib.request
    page = urllib.request.urlopen('http://bw.org/')
    print(page)
  
if __name__ == "__main__": main()



#### print and convert each line to a string
#### provide encoding

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    import urllib.request
    page = urllib.request.urlopen('http://bw.org/')
    for line in page: print(str(line, encoding = 'utf_8'), end = '')
  
if __name__ == "__main__": main()



#### Random module

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    import random
    print(random.randint(1,1000))
  
if __name__ == "__main__": main()



####  use the shuffle method

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    import random
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)
  
if __name__ == "__main__": main()

'''
####  datetime module

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second)
    
  
if __name__ == "__main__": main()



