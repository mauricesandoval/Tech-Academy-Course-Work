Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 'This is a string'
'This is a string'
>>> s = 'This is a string'
>>> s
'This is a string'
>>> s.upper()
'THIS IS A STRING'
>>> 'This is a string'.upper()
'THIS IS A STRING'
>>> 'This is a string'{}'.format(42)
SyntaxError: invalid syntax
>>> 'This is a string {}'.format(42)
'This is a string 42'
>>> 'This is a string %d' %42
'This is a string 42'
>>> 
