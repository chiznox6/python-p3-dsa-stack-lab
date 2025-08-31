class Stack:

    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit
        pass

    def isEmpty(self):
        pass
        return len(self.items) == 0

    def push(self, item):
        pass
        if not self.full():
            self.items.append(item)
        # Do nothing if stack is full

    def pop(self):
        pass
        if not self.isEmpty():
            return self.items.pop()
        return None  # Return None instead of raising exception

    def peek(self):
        pass
        if not self.isEmpty():
            return self.items[-1]
        return None
    
    def size(self):
        pass
        return len(self.items)

    def full(self):
        pass
        return len(self.items) >= self.limit

    def search(self, target):
        pass
        if target in self.items:
            # distance from top of stack
            return len(self.items) - 1 - self.items.index(target)
        return -1
