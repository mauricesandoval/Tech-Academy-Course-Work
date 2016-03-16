import sqlite3

#connect to database
conn = sqlite3.connect("CustomerOrders.db")
#specify cursor for database
c = conn.cursor()

#create table
def tableCreate():
    c.execute("CREATE TABLE stuffToPlot(ID INT, unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def dataEntry():
    c.execute("INSERT INTO stuffToPlot VALUES(1, 17655952181.288, '2013-04-14 10:09:41','Python Sentiment',5)")
    c.execute("INSERT INTO stuffToPlot VALUES(2, 13655953481.707, '2013-04-14 10:10:57','Python Sentiment',6)")
    c.execute("INSERT INTO stuffToPlot VALUES(3, 13623552181.513, '2013-04-14 10:13:04','Python Sentiment',4)")
    conn.commit()

