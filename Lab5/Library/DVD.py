from Library.LibraryItem import LibraryItem


class DVD(LibraryItem):

    def __init__(self, title, director, length):
        self._title = title
        self._director = director
        self._length = length

    def type(self):
        return "DVD"

    def title(self):
        return self._title

    def director(self):
        return self._director

    def length(self):
        return "The DVD is " + str(self._length) + " minutes long."
