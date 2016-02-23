Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 'this is a string'
'this is a string'
>>> s = 'this is a string'
>>> s
'this is a string'
>>> s.capitalize()
'This is a string'
>>> s.upper()
'THIS IS A STRING'
>>> s.lower()
'this is a string'
>>> 'THIS IS A STRING
SyntaxError: EOL while scanning string literal
>>> 'THIS IS A STRING'.lower()
'this is a string'
>>> 'tHiS is a StRinG'.swapcase()
'ThIs IS A sTrINg'
>>> s
'this is a string'
>>> s.find('is')
2
>>> s.replace('this', 'that')
'that is a string'
>>> s
'this is a string'
>>> id(s)
48463504
>>> newstring = s.upper()
>>> newstring
'THIS IS A STRING'
>>> id(newstring)
47847136
>>> s.strip()
'this is a string'
>>> '  this is a string  '.strip()
'this is a string'
>>> '   this is a string  '.rstrip()
'   this is a string'
>>> s1 = 'this is a string\n'
>>> s1
'this is a string\n'
>>> s1.strip()
'this is a string'
>>> sl.rstrip('\n')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    sl.rstrip('\n')
NameError: name 'sl' is not defined
>>> s1.rstrip('\n')
'this is a string'
>>> s.isalnum()
False
>>> 'thisisastring'.isalnum()
True
>>> 'thisisastring'.isalpha()
True
>>> '12345'.isdigit()
True
>>> s.isdigit()
False
>>> s.isprintable()
True
>>> 
