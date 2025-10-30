books_stock = {
    "The Great Gatsby": 10,
    "1984": 5,
    "To Kill a Mockingbird": 3,
    "Pride and Prejudice": 8
}

print(books_stock)
print(books_stock["1984"])  # Accessing 'value' by key

books_stock["The Great Gatsby"] = 12  # Updating stock

print(books_stock)
print(books_stock.items())

for book in books_stock:
    print(f"{book}: {books_stock[book]}")     

books_stock["superman"] = 4  # Adding a new book
print(books_stock)

if book in books_stock:
    del books_stock["superman"]  # Deleting a book
    print(books_stock)