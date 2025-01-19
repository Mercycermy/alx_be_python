from library_management import Book, Library

def setup_library():
    """Initializes the library with some books."""
    library = Library()
    books = [
        Book("Brave New World", "Aldous Huxley"),
        Book("1984", "George Orwell"),
    ]
    for book in books:
        library.add_book(book)
    return library

def display_books(library, message):
    """Displays available books with a custom message."""
    print(message)
    library.list_available_books()

def main():
    # Setup library
    library = setup_library()
    display_books(library, "Available books after setup:")

    # Check out a book
    book_to_checkout = "1984"
    print(f"\nChecking out '{book_to_checkout}'...")
    library.check_out_book(book_to_checkout)
    display_books(library, f"\nAvailable books after checking out '{book_to_checkout}':")

    # Return a book
    print(f"\nReturning '{book_to_checkout}'...")
    library.return_book(book_to_checkout)
    display_books(library, f"\nAvailable books after returning '{book_to_checkout}':")

if __name__ == "__main__":
    main()
