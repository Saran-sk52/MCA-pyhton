class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.ISBN}")

    def update_author(self, new_author):
        self.author = new_author

class Library:
    def __init__(self):
        self.books = []

    def add(self, book_name, author, copies):
        self.books.append({'book_name': book_name, 'author': author, 'copies': copies})

    def lend(self, book_name):
        for book in self.books:
            if book['book_name'] == book_name and book['copies'] > 0:
                book['copies'] -= 1
                print(f"Lending out '{book_name}'. Copies left: {book['copies']}")
                return
        print(f"Sorry, '{book_name}' is not available or out of stock.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("Available books:")
        for book in self.books:
            print(f"Title: {book['book_name']}, Author: {book['author']}, Copies: {book['copies']}")
            
book1 = Book("The Alchemist", "Paulo Coelho", "1234")
book2 = Book("1984", "George Orwell", "9876")

book1.display()
book2.display()

book1.update_author("P. Coelho")
book1.display()

library = Library()

library.add(book1.title, book1.author, 5)
library.add(book2.title, book2.author, 3)

library.display_books()

library.lend("1984")
library.lend("The Alchemist")

library.display_books()
