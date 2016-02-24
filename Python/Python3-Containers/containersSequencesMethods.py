Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> t = tuple( range(25) )
>>> t
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
>>> type(t)
<class 'tuple'>
>>> 10 in t
True
>>> 50 in t
False
>>> 50 not in t
True
>>> t[10]
10
>>> len(t)
25
>>> for i in t: print(i)

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
>>> x = list(range(20)
	 )
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 10 in x
True
>>> 20 in x
False
>>> for i in x: print (i)

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
>>> x[10] = 25
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> t.count(5)
1
>>> t.index(5)
5
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> x.append(100)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100]
>>> len(x)
21
>>> x.extend(range(20))
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> x.insert(0, 25)
>>> x
[25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> x.insert(12, 100)
>>> x
[25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 100, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> x.remove(12)
>>> x
[25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 100, 11, 13, 14, 15, 16, 17, 18, 19, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> del x[12]
>>> x
[25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 11, 13, 14, 15, 16, 17, 18, 19, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> x.pop()
19
>>> x
[25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 11, 13, 14, 15, 16, 17, 18, 19, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
>>> x.pop(0)
25
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 11, 13, 14, 15, 16, 17, 18, 19, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
>>> 
