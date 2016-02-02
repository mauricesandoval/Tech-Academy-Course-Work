import sqlite3

# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

# Get data from database
cursor = conn.execute("SELECT * from SIMPSON_INFO")

# Extract data from cursor
rows = cursor.fetchall()
print rows
