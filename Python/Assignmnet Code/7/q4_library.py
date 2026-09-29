class Book:
    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                print("Book borrowed successfully.")
                return
        print("Book is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.is_available = True
                print("Book returned successfully.")
                return
        print("Book not found.")

    def display_available_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.is_available:
                print(book.title, "-", book.author)


book1 = Book("Python Programming", "Guido van Rossum")
book2 = Book("The Alchemist", "Paulo Coelho")

library = Library()

library.add_book(book1)
library.add_book(book2)

library.display_available_books()

library.borrow_book("Python Programming")

library.display_available_books()

library.return_book("Python Programming")

library.display_available_books()