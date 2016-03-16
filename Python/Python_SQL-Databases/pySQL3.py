import sqlite3
import time
import datetime

#connect to database
conn = sqlite3.connect("CustomerOrders.db")
#specify cursor for database
c = conn.cursor()

sql = "SELECT * FROM stuffToPlot WHERE keyword =?"

wordUsed = 'Python Sentiment'

def readData():
    for row in c.execute(sql, [(wordUsed)]):
        print row
