# Importing Sqlite3.
import sqlite3

# Connect to SQLite database or create it if it doesn't exist.
connect = sqlite3.connect('book.db')
cursor = connect.cursor()

# Create a book table if it doesn't exist.
cursor.execute('''CREATE TABLE IF NOT EXISTS book (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    author TEXT,
                    quantity INTEGER)''')

# Importing data for the table with descriptions of the books.
books = [
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
    (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
]
# Using "executemany" to insert data into the table.
cursor.executemany('''INSERT OR IGNORE INTO book (id, title, author, quantity)
                    VALUES (?, ?, ?, ?)''', books)
connect.commit()


# Prompt for users to enter book details.
def enter_book():
    id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    quantity = int(input("Enter book quantity: "))

    cursor.execute('''INSERT INTO book (id, title, author, quantity)
                   VALUES (?, ?, ?, ?)''', (id, title, author, quantity))
    connect.commit()
    print("Your book added to the system.")


# Prompt for the users to update existing book details.
def update_book():
    id = int(input("Enter book ID to update: "))
    title = input("Enter new title: ")
    author = input("Enter new author: ")
    quantity = int(input("Enter new quantity: "))

    cursor.execute('''UPDATE book SET
                   title = ?, author = ?, quantity = ? WHERE id = ?''',
                   (title, author, quantity, id))
    connect.commit()
    print("This book has been updated.")


# Prompt for the user to delete a book for the database.
def delete_book():
    id = int(input("Enter book ID to delete: "))
    cursor.execute("DELETE FROM book WHERE id = ?", (id,))
    connect.commit()
    print("This book has been deleted.")


# Prompt for the user to search for existing books.
def search_books():
    id = int(input("Enter book ID to search: "))
    cursor.execute("SELECT * FROM book WHERE id = ?", (id,))
    book = cursor.fetchone()

    if book:
        print(f'''ID: {book[0]}, Title: {book[1]}, Author: {book[2]},
               Quantity: {book[3]}''')
    else:
        print("The book you were looking for was not found.")


def menu():
    while True:
        print("\nMenu:")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            enter_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_books()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid number.")


if __name__ == "__main__":
    menu()


connect.close()
