#creating a book class which has 3 aurguments
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
#creating a child class of ebook ehich inerits from the Book class
class EBook(Book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author,)
        self.file_size = file_size
       # return f"{super().__str__()} (File size: {self.file_size} MB)"
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"   

 #creating another child class which also inherits from the  Book class
class PrintBook(Book):
    def __init__(self,title,author,page_count):
        super().__init__(title,author) 
        self.page_count = page_count
        #return f"{super().__str__()} (Pages: {self.page_count})"
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author},  Page Count: {self.page_count}"   


 
# implement a Library class demonstrating composition by managing a collection of books.
class Library:
    def __init__(self):
        """Initialize an empty library with a list to store books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        if isinstance(book, Book):
            self.books.append(book)
            #print(book)
        else:
            print("Only instances of Book or its subclasses can be added.")

    def list_books(self):
        """Print details of each book in the library."""
        if not self.books:
            print("No books in the library.")
           #return
       # print("Books in Library:")
        for book in self.books:
            print(book)
