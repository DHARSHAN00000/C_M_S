import sqlite3


# Function to connect to the SQLite database
def connect_to_database():
    connection = sqlite3.connect("contact_book.db")
    cursor = connection.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            CellNumber TEXT,
            Email TEXT
        )
    ''')

    return connection, cursor


# Function to insert data into the database
def insert_data(connection, cursor, name, cell_number, email):
    cursor.execute('''
        INSERT INTO contacts (Name, CellNumber, Email) VALUES (?, ?, ?)
    ''', (name, cell_number, email))
    connection.commit()


# Function to fetch and display all data from the database
def fetch_and_display_data(cursor):
    cursor.execute('SELECT * FROM contacts')
    data = cursor.fetchall()

    if not data:
        print("No contacts found.")
    else:
        print("ID\tName\t\tCell#\t\tE-mail")
        print("-" * 40)
        for row in data:
            print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}")


# Main function
def main():
    connection, cursor = connect_to_database()

    # Insert 5 rows of data
    insert_data(connection, cursor, "Darshan", "8971021242", "dhtr@example.com")
    insert_data(connection, cursor, "vidya", "9876543210", "vibn@example.com")
    insert_data(connection, cursor, "ruchita", "5555555555", "ruch@example.com")
    insert_data(connection, cursor, "varsha", "7777777777", "varh@example.com")
    insert_data(connection, cursor, "divya", "9999999999", "dips@example.com")

    # Fetch and display all data
    fetch_and_display_data(cursor)

    # Close the connection
    connection.close()


if __name__ == "__main__":
    main()

