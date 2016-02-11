Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 42
>>> x
42
>>> id(x)
1402157472
>>> type(x)
<class 'int'>
>>> id(42)
1402157472
>>> type(42)
<class 'int'>
>>> y = 42
>>> id(y)
1402157472
>>> x == y
True
>>> x is y
True
>>> x = dict(x = 42)
>>> type(x)
<class 'dict'>
>>> x
{'x': 42}
>>> id(x)
48103712
>>> y = dict(x = 42)
>>> id(y)
48103992
>>> x
{'x': 42}
>>> y
{'x': 42}
>>> x == y
True
>>> x is y
False
>>> 
