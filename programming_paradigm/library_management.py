class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False  # Starts as not checked out

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not checked out.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"'{book.title}' by {book.author} added to the library.")
        else:
            print("Only instances of the Book class can be added.")

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_checked_out:
                book.check_out()
                return
        print(f"'{title}' is either not available or already checked out.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_checked_out:
                book.return_book()
                return
        print(f"'{title}' is either not checked out or not in the library.")

    def list_available_books(self):
        available_books = [book for book in self.books if not book.is_checked_out]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No books are currently available.")



