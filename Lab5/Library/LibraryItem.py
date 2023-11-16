
class LibraryItem:

    def type(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def title(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def author(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def length(self):
        raise NotImplementedError("Subclass must implement abstract method")