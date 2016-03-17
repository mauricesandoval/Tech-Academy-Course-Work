import sqlite3

#connect to database
conn = sqlite3.connect("CustomerOrderList.db")
#specify cursor for database
c = conn.cursor()

#create table
def tableCreate():
    c.execute("CREATE TABLE fileCheck(ID INT, datestamp TEXT, keyword TEXT)")


    conn.commit()

