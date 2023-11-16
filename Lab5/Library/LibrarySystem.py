from Library.LibraryItem import LibraryItem


class LibrarySystem:

    def __init__(self):
        self._library_items = []
        self._checked_out_items = []

    def display_library_items(self):
        for item in self._library_items:
            print(item.type() + ": " + item.title())

    def add_library_item(self, item):
        self._library_items.append(item)

    def remove_library_item(self, item):
        self._library_items.remove(item)

    def checkout_library_item(self, item):
        self._checked_out_items.append(item)
        self._library_items.remove(item)

    def return_library_item(self, item):
        self._checked_out_items.remove(item)
        self._library_items.append(item)
