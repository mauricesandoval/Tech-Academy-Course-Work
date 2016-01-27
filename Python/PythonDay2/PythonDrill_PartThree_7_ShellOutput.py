Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: C:\Python27\pythonDay2Databases.py ================

Traceback (most recent call last):
  File "C:\Python27\pythonDay2Databases.py", line 14, in <module>
    );")
OperationalError: table SIMPSON_INFO already exists
>>> 
================ RESTART: C:/Python27/pythonDay2Databases2.py ================
>>> 
================ RESTART: C:/Python27/pythonDay2Databases2.py ================
Number of changes: 1
>>> 
================ RESTART: C:/Python27/pythonDay2Databases3.py ================
Number of changes: 2
>>> 
================ RESTART: C:/Python27/pythonDay2Databases4.py ================
<sqlite3.Cursor object at 0x029D6CE0>
>>> 
================ RESTART: C:/Python27/pythonDay2Databases5.py ================
[(1, u'Homer Simpson', u'Male', 40, u'Nuclear Plant'), (2, u'Lisa Simpson', u'Female', 8, u'Student')]
>>> 
================ RESTART: C:/Python27/pythonDay2Databases6.py ================
Results for Homer Simpson:
[(1, u'Homer Simpson', u'Male', 40, u'Nuclear Plant')]
Results for Females:
[(2, u'Lisa Simpson', u'Female', 8, u'Student')]
Results for Students:
[(2, u'Lisa Simpson', u'Female', 8, u'Student')]
>>> 
================ RESTART: C:/Python27/pythonDay2Databases7.py ================
Number of changes:  1
[(1, u'Homer Simpson', u'Male', 40, u'Nuclear Plant')]
>>> 
