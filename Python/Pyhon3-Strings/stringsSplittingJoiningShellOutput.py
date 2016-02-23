Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = 'This is a string of words'
>>> s.split()
['This', 'is', 'a', 'string', 'of', 'words']
>>> 'This  is   a   string   of   words'.split()
['This', 'is', 'a', 'string', 'of', 'words']
>>> s.split('i')
['Th', 's ', 's a str', 'ng of words']
>>> words = s.split()
>>> words
['This', 'is', 'a', 'string', 'of', 'words']
>>> for w in words: print(w)

This
is
a
string
of
words
>>> new = ':'.join(words)
>>> new
'This:is:a:string:of:words'
>>> ','.join(words)
'This,is,a,string,of,words'
>>> 
