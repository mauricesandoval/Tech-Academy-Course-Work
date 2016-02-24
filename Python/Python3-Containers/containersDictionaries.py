Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> d = {'one' : 1, 'two' : 2, 'three' : 3}
>>> d
{'three': 3, 'two': 2, 'one': 1}
>>> d = dict ( one = 1, two = 2, three = 3 )
>>> d
{'three': 3, 'two': 2, 'one': 1}
>>> type(d)
<class 'dict'>
>>> x = dict ( four = 4, five = 5, six = 6 )
>>> x
{'five': 5, 'four': 4, 'six': 6}
>>> d = dict ( one = 1, two = 2, three = 3, **x)
>>> d
{'five': 5, 'three': 3, 'six': 6, 'two': 2, 'four': 4, 'one': 1}
>>> 'four' in x
True
>>> 'three' in x
False
>>> for k in d: print(k)

five
three
six
two
four
one
>>> for k, v in d.items(): print(k, v)

five 5
three 3
six 6
two 2
four 4
one 1
>>> d['three']
3
>>> x.get('three')
>>> 
>>> d.get('three')
3
>>> x.get('three', 'not found')
'not found'
>>> x
{'five': 5, 'four': 4, 'six': 6}
>>> del x['four]
      
SyntaxError: EOL while scanning string literal
>>> del x['four']
>>> x
{'five': 5, 'six': 6}
>>> x.pop('five')
5
>>> x
{'six': 6}
>>> 
