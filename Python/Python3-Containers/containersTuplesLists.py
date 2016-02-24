Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> t = 1,2,3,4,5
>>> t
(1, 2, 3, 4, 5)
>>> t[0]
1
>>> t[4]
5
>>> t[-1]
5
>>> len(t)
5
>>> min(t)
1
>>> max(t)
5
>>> t = (1, 2, 3, 4, 5)
>>> t = (1)
>>> t
1
>>> type(t)
<class 'int'>
>>> t = (1,)
>>> t
(1,)
>>> type(t)
<class 'tuple'>
>>> x = [1, 2, 3, 4, 5]
>>> x
[1, 2, 3, 4, 5]
>>> type[x]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    type[x]
TypeError: 'type' object is not subscriptable
>>> type(x)
<class 'list'>
>>> x[0]
1
>>> xx[-1]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    xx[-1]
NameError: name 'xx' is not defined
>>> x[-1]
5
>>> len(x)
5
>>> min(x)
1
>>> max(x)
5
>>> t
(1,)
>>> t = tuple(range(25))
>>> t
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
>>> type(t)
<class 'tuple'>
>>> t{10} = 42
SyntaxError: invalid syntax
>>> t[10] = 42
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    t[10] = 42
TypeError: 'tuple' object does not support item assignment
>>> x = list(range(25))
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
>>> type(x)
<class 'list'>
>>> x[10] = 42
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 42, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
>>> 
