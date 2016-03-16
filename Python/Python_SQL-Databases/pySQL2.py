import sqlite3
import time
import datetime

#connect to database
conn = sqlite3.connect("CustomerOrders.db")
#specify cursor for database
c = conn.cursor()

#create table
def tableCreate():
    c.execute("CREATE TABLE stuffToPlot(ID INT, unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

    
idfordb = 4
keyword = 'Python Sentiment'
value = 7

    

def dataEntry():
    date  = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO stuffToPlot (ID, unix, datestamp, keyword, value) VALUES (?,?,?,?,?)",
              (idfordb, time.time(), date, keyword, value))
       
    conn.commit()

