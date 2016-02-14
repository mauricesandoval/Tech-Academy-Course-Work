Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 5
5
>>> 0b0101
5
>>> def b(n): print('{:08b}'.format(n))

>>> b(5)
00000101
>>> x, y = 0x55, 0xaa
>>> b(y)
10101010
>>> b(x)
01010101
>>> b(x | y)
11111111
>>> b(x & y)
00000000
>>> b(x ^ y)
11111111
>>> b(x ^ 0)
01010101
>>> b(x ^ 0xff)
10101010
>>> b(x << 4)
10101010000
>>> b(x >> 4)
00000101
>>> b(~ x)
-1010110
>>> 
