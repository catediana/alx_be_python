#creating a book class which accepts three aurguments
class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
#using the del magic method
    def __del__(self):
        print(f"Deleting { self.title}")

#using the __str__magic method to return a formated string
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

#usint the __repe__magic method to format the return statement
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"



