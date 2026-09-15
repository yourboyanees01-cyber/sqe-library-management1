class Book:
    """Represents a single book in the library catalog."""

    def __init__(self, title, isbn, author, total_copies):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.total_copies = total_copies