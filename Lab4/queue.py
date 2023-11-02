class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[0]

    def is_empty(self):
        return self.items == []