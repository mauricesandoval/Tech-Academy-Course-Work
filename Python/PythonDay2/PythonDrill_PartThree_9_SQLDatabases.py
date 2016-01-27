#####
##### Delete a Table in the Database
#####

import sqlite3

# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

# Delete the table
conn.execute("DROP TABLE SIMPSON_INFO")

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

