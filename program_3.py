import sqlite3


def main():
    # Connect to the database.
    conn = sqlite3.connect('phonebook.db')

    # Get a database cursor.
    cur = conn.cursor()

    # Add the Entries table.
    entries_table(cur)

    # Add rows to the phonebook table.
    add_phonebook(cur)

    # Commit the changes.
    conn.commit()

    # Display the entries.
    display_entries(cur)

    # Close the connection.
    conn.close()


# The entries_table adds the Entries table to the database.
def entries_table(cur):
    # If the table already exists, drop it.
    cur.execute('DROP TABLE IF EXISTS Entries')

    # Create the table.
    cur.execute('''CREATE TABLE Entries (Phone_number TEXT PRIMARY KEY NOT NULL,
                                        Name TEXT)''')


# The add_cities function adds 20 rows to the Cities table.
def add_phonebook(cur):
    entries_pop = [("612-623-9733", 'Charlie Anderson'),
                  ("763-224-7674", 'Leah Johnson'),
                  ("320-770-7472", 'Molly Stevens'),
                   ("763'543-9876", 'Sally Brown'),
                   ("612-876-3456", 'John Smith'),
                   ("612-087-4737", 'Kevin Jones')]

    for row in entries_pop:
        cur.execute('''INSERT INTO Entries (Phone_number, Name)
                       VALUES (?, ?)''', (row[0], row[1]))


# The display_cities function displays the contents of
# the Phonebook table.
def display_entries(cur):
    print('Contents of phonebook.db/Entries table:')
    cur.execute('SELECT * FROM Entries')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<3} {row[1]:20}')


# Execute the main function.
if __name__ == '__main__':
    main()