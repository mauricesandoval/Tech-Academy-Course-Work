import sqlite3

# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

# Add Bart Simpson to table
conn.execute("INSERT INTO SIMPSON_INFO \
(NAME, GENDER, AGE, OCCUPATION) VALUES \
('Bart Simpson', 'Male', 10, 'Student')");

#Save Changes
conn.commit

# Print number of changes to database
changes = conn.total_changes
print "Number of changes:", changes
