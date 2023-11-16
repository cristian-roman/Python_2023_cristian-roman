from Library.LibraryItem import LibraryItem


class Magazine(LibraryItem):

    def __init__(self, title, publisher, number_of_pages):
        self._title = title
        self._publisher = publisher
        self._number_of_pages = number_of_pages

    def type(self):
        return "Magazine"

    def title(self):
        return self._title

    def publisher(self):
        return self._publisher

    def length(self):
        return "The magazine has " + str(self._number_of_pages) + " pages."
