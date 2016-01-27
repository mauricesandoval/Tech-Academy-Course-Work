#####
#####  Inserting Data into the Database
#####

import sqlite3

# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

# Add Homer Simpson to table
conn.execute("INSERT INTO SIMPSON_INFO \
    (NAME, GENDER, AGE, OCCUPATION) VALUES \
    ('Homer Simpson', 'Male', 40, 'Nuclear Plant')");

# Add Lisa Simpson to table
conn.execute("INSERT INTO SIMPSON_INFO \
    (NAME, GENDER, AGE, OCCUPATION) VALUES \
    ('Lisa Simpson', 'Female', 8, 'Student')");

# Save changes
conn.commit()

# Print number of changes to database
changes = conn.total_changes
print "Number of changes:", changes
