from mylibrary.library import Library


if __name__ == "__main__":
    library = Library()
    library.add_book("Book One", "Author One")
    library.add_book("Book Two", "Author Two")
    library.show_books()
