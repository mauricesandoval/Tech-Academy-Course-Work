Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 5 < 6
True
>>> 6 < 5
False
>>> 5 <= 6
True
>>> 5 <= 5
True
>>> 6 >= 5
True
>>> 6 >= 6
True
>>> 6 >= 7
False
>>> 5 == 5
True
>>> 5 == 6
False
>>> 6 != 7
True
>>> 6 != 6
False
>>> x, y = 5, 6
>>> id(x)
1901016912
>>> id(y)
1901016928
>>> x is y
False
>>> x is not y
True
>>> y = 5
>>> id(y)
1901016912
>>> id(x)
1901016912
>>> x is y
True
>>> x, y = [5], [5]
>>> id(x)
48338704
>>> id(y)
47918976
>>> x = y
>>> x == y
True
>>> x is y
True
>>> 
