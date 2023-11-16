from Library.LibraryItem import LibraryItem


class Book(LibraryItem):

    def __init__(self, title, author, number_of_pages):
        self._title = title
        self._author = author
        self._number_of_pages = number_of_pages

    def type(self):
        return "Book"

    def title(self):
        return self._title

    def author(self):
        return self._author

    def length(self):
        return "The book has " + str(self._number_of_pages) + " pages."
