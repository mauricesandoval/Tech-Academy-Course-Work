Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Student/AppData/Local/Programs/Python/Python35-32/Ex_Files_Python_3_EssT/Exercise Files/16 Databases/databasesSQLite3.py 
This is the databases.py file
>>> 
 RESTART: C:/Users/Student/AppData/Local/Programs/Python/Python35-32/Ex_Files_Python_3_EssT/Exercise Files/16 Databases/databasesSQLite3.py 
>>> 
 RESTART: C:/Users/Student/AppData/Local/Programs/Python/Python35-32/Ex_Files_Python_3_EssT/Exercise Files/16 Databases/databasesSQLite3.py 
Traceback (most recent call last):
  File "C:/Users/Student/AppData/Local/Programs/Python/Python35-32/Ex_Files_Python_3_EssT/Exercise Files/16 Databases/databasesSQLite3.py", line 47, in <module>
    if __name__ == "__main__": main()
  File "C:/Users/Student/AppData/Local/Programs/Python/Python35-32/Ex_Files_Python_3_EssT/Exercise Files/16 Databases/databasesSQLite3.py", line 36, in main
    db.execute('insert into test (t1, i1) values (?, ?)', ('one', 1))
sqlite3.OperationalError: table test has no column named i1
>>> 
 RESTART: C:/Users/Student/AppData/Local/Programs/Python/Python35-32/Ex_Files_Python_3_EssT/Exercise Files/16 Databases/databasesSQLite3.py 
('four', 4)
('one', 1)
('three', 3)
('two', 2)
>>> 
 RESTART: C:/Users/Student/AppData/Local/Programs/Python/Python35-32/Ex_Files_Python_3_EssT/Exercise Files/16 Databases/databasesSQLite3.py 
(1, 'one')
(2, 'two')
(3, 'three')
(4, 'four')
>>> 
 RESTART: C:/Users/Student/AppData/Local/Programs/Python/Python35-32/Ex_Files_Python_3_EssT/Exercise Files/16 Databases/databasesSQLite3.py 
<sqlite3.Row object at 0x02D931A0>
<sqlite3.Row object at 0x02D93390>
<sqlite3.Row object at 0x02D931A0>
<sqlite3.Row object at 0x02D93390>
>>> 
 RESTART: C:/Users/Student/AppData/Local/Programs/Python/Python35-32/Ex_Files_Python_3_EssT/Exercise Files/16 Databases/databasesSQLite3.py 
{'i1': 1, 't1': 'one'}
{'i1': 2, 't1': 'two'}
{'i1': 3, 't1': 'three'}
{'i1': 4, 't1': 'four'}
>>> 
 RESTART: C:/Users/Student/AppData/Local/Programs/Python/Python35-32/Ex_Files_Python_3_EssT/Exercise Files/16 Databases/databasesSQLite3.py 
Traceback (most recent call last):
  File "C:/Users/Student/AppData/Local/Programs/Python/Python35-32/Ex_Files_Python_3_EssT/Exercise Files/16 Databases/databasesSQLite3.py", line 131, in <module>
    if __name__ == "__main__": main()
  File "C:/Users/Student/AppData/Local/Programs/Python/Python35-32/Ex_Files_Python_3_EssT/Exercise Files/16 Databases/databasesSQLite3.py", line 129, in main
    print(row['t1'], roe['i1']) #### change here
NameError: name 'roe' is not defined
>>> 
 RESTART: C:/Users/Student/AppData/Local/Programs/Python/Python35-32/Ex_Files_Python_3_EssT/Exercise Files/16 Databases/databasesSQLite3.py 
one 1
two 2
three 3
four 4
>>> 
