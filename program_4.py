import sqlite3

def main():
    #connect the phonebook database
    conn = sqlite3.connect('phonebook.db')

    #get a cursor
    cur = conn.cursor()

    #get name from user
    phone_name = input("Enter a name to search for or hit enter to see all: ")

    if phone_name == '':
        cur.execute("SELECT Name, Phone_number from Entries")
        results = (cur.fetchall())
        print(f'The current information is {results}')

    else:
        cur.execute("SELECT Name, Phone_number from Entries WHERE Name = '" + phone_name + "'")
        results = (cur.fetchone())
        if results == None:
            print("No one by the name '" + phone_name + "' was found.")
            return
        else:
            print(results)
            delete = input('Would you like to delete the entry? (y/n) ')
            if delete.lower() == 'y':
                cur.execute("DELETE FROM Entries WHERE Name = ?", (phone_name,))
                conn.commit()
                print(f'The entry {phone_name} was successfully deleted.')
                return

            update = input('Would you like to update the phone number? (y/n) ')
            if update.lower() == 'y':
                new_number = input("Enter the new phone number: ")
                # Update number
                cur.execute("UPDATE Entries SET Phone_number=? WHERE Name == ? ",(new_number, phone_name))
                conn.commit()
                print('The phone number was successfully updated.')


    #Close the connection
    conn.close()

if __name__ == '__main__':
        main()