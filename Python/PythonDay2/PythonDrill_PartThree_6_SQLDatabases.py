#####
#####  Viewing Specific Data
#####

import sqlite3

# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

# Searching by character name
# Get data from database
cursor = conn.execute("SELECT * from SIMPSON_INFO where NAME='Homer Simpson'")

# Extract data from cursor
rows = cursor.fetchall()
print 'Results for Homer Simpson:'
print rows

# Searching for females
# Get data from database
cursor = conn.execute("SELECT * from SIMPSON_INFO where GENDER='Female'")

# Extract data from cursor
rows = cursor.fetchall()
print 'Results for Females:'
print rows

# Searching for students
# Get data from database
cursor = conn.execute("SELECT * from SIMPSON_INFO where OCCUPATION='Student'")

# Extract data from cursor
rows = cursor.fetchall()
print 'Results for Students:'
print rows
