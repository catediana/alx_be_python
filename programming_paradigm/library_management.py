# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out

    

class Library:
   
    def __init__(self):
        # Initialize a private list to store books
        self._books = []

    def add_book(self, book):
        """
        Adds a book to the library after ensuring it has the correct attributes.
        """
        try:
            # Check if the book has the required attributes (title, author)
             # Validate that the book has the required attributes
            book_title = book.title  # Access book title to ensure it's present
            book_author = book.author  # Access book author to ensure it's present
            self._books.append(book)
        except AttributeError:
            print("Error: Only objects of the 'Book' class can be added.")

    def check_out_book(self, title):
        """
        Marks a book as checked out by title if it's available.
        """
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                print(f"'{title}' has been checked out.")
                return
        print(f"Error: '{title}' is either not in the library or already checked out.")

    def return_book(self, title):
        """
        Marks a book as returned by title if it is currently checked out.
        """
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                print(f"'{title}' has been returned.")
                return
        print(f"Error: '{title}' is either not in the library or not checked out.")

    def list_available_books(self):
        """
        Lists all books in the library that are not currently checked out.
        """
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
