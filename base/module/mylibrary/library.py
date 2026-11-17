class Library:
    list_of_books = []

    def __init__(self):
        self.list_of_books = []

    def add_book(self, title, author):
        self.list_of_books.append({"title": title, "author": author})

    def remove_book(self, title):
        self.list_of_books = [book for book in self.list_of_books if book["title"] != title]
    
    def search_book(self, title):
        return [book for book in self.list_of_books if book["title"] == title]

    def show_books(self):
        for book in self.list_of_books:
            print(f'Title: {book["title"]}, Author: {book["author"]}')