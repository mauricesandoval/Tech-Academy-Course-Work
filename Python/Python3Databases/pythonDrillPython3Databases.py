import sqlite3

# Create a temporary database connection in RAM
connection = sqlite3.connect(':memory:')

    c = connection.cursor()

    # Create a "Roster" table with Name, Species and IQ fields
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")

    # Add some data into the database
    c.execute("INSERT INTO Roster VALUES('Jean-Baptiste Zorg', 'Human', '122')")

    connection.commit()

    c.execute("INSERT INTO Roster VALUES('Korben Dallas', 'Meat Popsicle', '100')")

    connection.commit()

    c.execute("""INSERT INTO Roster VALUES("Ak'not", 'Mangalore', '-5')""")

    connection.commit()

    # Update the Species of Korben Dallas to "Human"
    c.execute("UPDATE Roster SET Name=? WHERE Species=? AND IQ=?", ('Korben Dallas', 'Human', '100'))

    # Display the names and IQs of everyone classified as Human
    c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
    for row in c.fetchall():

        print row
