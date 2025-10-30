# ALGORITHM
# STEP 1: Start.
# STEP 2: Initialize a dictionary with book titles and stock. 
# STEP 3: Display menu options to:
#    ●Update stock.
#    ● Add a new book.
#    ● Delete a book.
# STEP 4: Perform the selected operation and display the updated dictionary. 
# STEP 5: Repeat until the user chooses to exit.
# STEP 6: Stop.




# Creating a dictionary with book titles and their stock
books_stock = {
    "The Great Gatsby": 10,
    "1984": 5,
    "To Kill a Mockingbird": 3,
    "Pride and Prejudice": 8
}

# Function to display the current books and stock
def display_books():
    print("\nCurrent Books in Stock:")
    for book, stock in books_stock.items():
        print(f"{book}: {stock} copies")

# Function to update the stock of a book
def update_stock(book, stock_change):
    if book in books_stock:
        books_stock[book] += stock_change
        print(f"\nStock of '{book}' updated. New stock: {books_stock[book]}")
    else:
        print(f"\n'{book}' not found in the dictionary.")

# Function to add a new book to the inventory
def add_book(book, stock):
    if book not in books_stock:
        books_stock[book] = stock
        print(f"\n'{book}' has been added to the inventory with {stock} copies.")
    else:
        print(f"\n'{book}' already exists in the inventory.")

# Function to delete a book from the inventory
def delete_book(book):
    if book in books_stock:
        del books_stock[book]
        print(f"\n'{book}' has been deleted from the inventory.")
    else:
        print(f"\n'{book}' not found in the inventory.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display current books and stock")
    print("2. Update stock")
    print("3. Add new book")
    print("4. Delete book")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        display_books()

    elif choice == '2':
        book_title = input("\nEnter the title of the book to update: ")
        stock_change = int(input(f"Enter the change in stock for '{book_title}': "))
        update_stock(book_title, stock_change)

    elif choice == '3':
        book_title = input("\nEnter the title of the new book: ")
        stock = int(input(f"Enter the stock for '{book_title}': "))
        add_book(book_title, stock)

    elif choice == '4':
        book_title = input("\nEnter the title of the book to delete: ")
        delete_book(book_title)

    elif choice == '5':
        print("\nExiting the program.")
        break

    else:
        print("\nInvalid choice. Please try again.")