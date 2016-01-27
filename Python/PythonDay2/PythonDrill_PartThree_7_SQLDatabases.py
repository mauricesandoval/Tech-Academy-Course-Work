#####
#####  Deleting Data from the Database
#####

import sqlite3

# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

# Delete rows with ID=2
conn.execute("DELETE from SIMPSON_INFO where ID=2")

# Save changes
conn.commit()

# Print number of changes
changes = conn.total_changes
print "Number of changes: ",changes

# Get data from database
cursor = conn.execute("SELECT * from SIMPSON_INFO")

# Extract data from cursor
rows = cursor.fetchall()
print rows

