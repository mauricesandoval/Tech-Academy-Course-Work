import sqlite3

# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

# Get data from database
cursor = conn.execute("SELECT ID, NAME, GENDER, AGE, OCCUPATION from SIMPSON_INFO")
print cursor

