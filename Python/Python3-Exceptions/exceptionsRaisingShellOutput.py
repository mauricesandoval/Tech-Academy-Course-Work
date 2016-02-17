Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Student/Desktop/Ex_Files_Python_3_EssT/Exercise Files/10 Exceptions/exceptionsRaising.py 
01 This is a line of text
02 This is a line of text
03 This is a line of text
04 This is a line of text
05 This is a line of text
>>> 
 RESTART: C:/Users/Student/Desktop/Ex_Files_Python_3_EssT/Exercise Files/10 Exceptions/exceptionsRaising.py 
01 This is a line of text
02 This is a line of text
03 This is a line of text
04 This is a line of text
05 This is a line of text
>>> 
 RESTART: C:/Users/Student/Desktop/Ex_Files_Python_3_EssT/Exercise Files/10 Exceptions/exceptionsRaising.py 
Traceback (most recent call last):
  File "C:/Users/Student/Desktop/Ex_Files_Python_3_EssT/Exercise Files/10 Exceptions/exceptionsRaising.py", line 39, in <module>
    if __name__ == "__main__": main()
  File "C:/Users/Student/Desktop/Ex_Files_Python_3_EssT/Exercise Files/10 Exceptions/exceptionsRaising.py", line 33, in main
    for line in readfile('xlines.txt'): print(line.strip())
  File "C:/Users/Student/Desktop/Ex_Files_Python_3_EssT/Exercise Files/10 Exceptions/exceptionsRaising.py", line 36, in readfile
    fh = open(filename)
FileNotFoundError: [Errno 2] No such file or directory: 'xlines.txt'
>>> 
 RESTART: C:/Users/Student/Desktop/Ex_Files_Python_3_EssT/Exercise Files/10 Exceptions/exceptionsRaising.py 
cannot read file: [Errno 2] No such file or directory: 'xlines.txt'
>>> 
 RESTART: C:/Users/Student/Desktop/Ex_Files_Python_3_EssT/Exercise Files/10 Exceptions/exceptionsRaising.py 
cannot read file: [Errno 2] No such file or directory: 'xlines.txt'
>>> 
 RESTART: C:/Users/Student/Desktop/Ex_Files_Python_3_EssT/Exercise Files/10 Exceptions/exceptionsRaising.py 
Traceback (most recent call last):
  File "C:/Users/Student/Desktop/Ex_Files_Python_3_EssT/Exercise Files/10 Exceptions/exceptionsRaising.py", line 73, in <module>
    if __name__ == "__main__": main()
  File "C:/Users/Student/Desktop/Ex_Files_Python_3_EssT/Exercise Files/10 Exceptions/exceptionsRaising.py", line 63, in main
    for line in readfile('xlines.doc'): print(line.strip())
  File "C:/Users/Student/Desktop/Ex_Files_Python_3_EssT/Exercise Files/10 Exceptions/exceptionsRaising.py", line 71, in readfile
    else: raise ValueError('Filename must end with .txt')
ValueError: Filename must end with .txt
>>> 
 RESTART: C:/Users/Student/Desktop/Ex_Files_Python_3_EssT/Exercise Files/10 Exceptions/exceptionsRaising.py 
bad filenname Filename must end with .txt
>>> 
