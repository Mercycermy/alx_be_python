class Book:
    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to delete the book instance and print a message."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation of the book that can recreate the instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"