#####
#####  Inserting Data into the Database
#####

import sqlite3

# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

# Add Bart Simpson to table
conn.execute("INSERT INTO SIMPSON_INFO \
    (NAME, GENDER, AGE, OCCUPATION) VALUES \
    ('Bart Simpson', 'Male', 10, 'Student' )");

# Save changes
conn.commit()
