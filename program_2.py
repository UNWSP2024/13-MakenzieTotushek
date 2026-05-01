import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('cities.db')

    # Get a database cursor.
    cur = conn.cursor()

    # Display the cities.
    display_cities(cur)

    # Close the connection.
    conn.close()



# The display_cities function displays the contents of
# the Cities table.
def display_cities(cur):
    print('Contents of cities.db/Cities table:')
    cur.execute('SELECT * FROM Cities')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')


# Execute the main function.
if __name__ == '__main__':
    main()
