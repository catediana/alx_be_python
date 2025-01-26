#creating a book class which has 3 aurguments
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

#creating a child class of ebook ehich inerits from the Book class
class EBook(Book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author,)
        self.file_size = file_size

 #creating another child class which also inherits from the  Book class
class PrintBook(Book):
    def __init__(self,title,author,page_count):
        super().__init__(title,author) 
        self.page_count = page_count

# implement a Library class demonstrating composition by managing a collection of books.
class Library:
    def __init__(self):
        """Initialize an empty library with a list to store books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added: {book}")
        else:
            print("Only instances of Book or its subclasses can be added.")

    def list_books(self):
        """Print details of each book in the library."""
        if not self.books:
            print("No books in the library.")
            return
        print("Books in Library:")
        for book in self.books:
            print(book)
