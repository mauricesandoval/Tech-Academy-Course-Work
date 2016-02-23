Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a, b = 5, 42
>>> print(a, b)
5 42
>>> s = 'this is {}, that is {}'
>>> s
'this is {}, that is {}'
>>> s.format(a, b)
'this is 5, that is 42'
>>> id(s)
48297744
>>> new = s.format(a, b)
>>> id(new)
48297696
>>> s = 'this is {}, that is {}'.format(b, a)
>>> s
'this is 42, that is 5'
>>> s = 'this is {1}, that is {0}'.format(a, b)
>>> s
'this is 42, that is 5'
>>> 'this is {1}, that is {0}, this too is {1}'.format(a, b)
'this is 42, that is 5, this too is 42'
>>> 'this is {Bob}, that is {Fred}'.format(Bob = a, Fred = b)
'this is 5, that is 42'
>>> d = dict(Bob = a, Fred = b)
>>> 'this is {Bob}, that is {Fred}'.format(**d)
'this is 5, that is 42'
>>> 
