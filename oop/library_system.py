#creating a book class which has 3 aurguments
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

#creating a child class of ebook ehich inerits from the Book class
class EBook:
    def __init__(self,file_size,):
        super().__init__(title,author,)
        self.file_size = file_size

 #creating another child class which also inherits from the  Book class
class PrintBook:
    def __init__(self,page_count):
        supre().__init__(title,author) 
        self.page_count = page_count

# implement a Library class demonstrating composition by managing a collection of books.
class Library:
    def __init__(self,):
        self.books = [Book, EBook, PrintBook]

        def add_books(self,book):
            if isinstance (book,Books):
                self.books.append(book)
                print(f"added{book}")
            else:
                print("Only book in instance of Book or its subclass are to be added") 

    def list_books(self):
        """Print details of each book in the library."""
        if not self.books:
            print("No books in the library.")
            return
        print("Books in Library:")
        for book in self.books:
            print(book)
