class CustomQueue:
    def __init__(self):
        self.collection = []

    def enqueue(self, value):
        return self.collection.insert(len(self.collection), value)

    def dequeue(self):
        return self.collection.pop(0)

    def front(self):
        return self.collection[0]

    def size(self):
        return len(self.collection)

    def isEmpty(self):
        return len(self.collection) == 0


test = CustomQueue()
test.enqueue(5)
test.enqueue(6)
test.enqueue(7)

print(test.front())
print(test.size())
print(test.isEmpty())
test.dequeue()
print(test.front())
