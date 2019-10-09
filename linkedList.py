class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getValue(self):
        return self.data

    def getNext(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            return True
        else:
            node = self.head

            while node.next is not None:
                node = node.next

            node.next = Node(data)
            return True

        return False

    def remove(self, data):
        if self.head is None:
            return False

        if self.head.data is data:
            self.head = self.head.next
            return True
        else:
            prev = None
            node = self.head

            while node is not None:
                if node.data is data:
                    break

                prev = node
                node = node.next

            if node.data is data:
                prev.next = node.next
                return True
            else:
                return False

    def removeIndex(self, index):
        if self.head is None:
            return False

        if index is 0:
            self.head = self.head.next
            return True
        else:
            counter = 0
            prev = None
            node = self.head

            while node is not None:
                if counter is index:
                    break

                counter += 1
                prev = node
                node = node.next

            prev.next = node.next
            return True

    def indexOf(self, data):
        if self.head is None:
            return -1

        if self.head.data is data:
            return 0
        else:
            index = 0
            node = self.head

            while node is not None:
                if node.data is data:
                    return index

                index += 1
                node = node.next

        return index

    def elementAt(self, index):
        if self.head is None:
            return None

        if index is 0:
            return self.head
        else:
            counter = 0
            node = self.head

            while node is not None:
                if counter is index:
                    break

                counter += 1
                node = node.next

            return node

    def reverse(self):
        if self.head is None:
            return False

        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev
        return True


test = LinkedList()
test.add(5)
test.add(6)
test.add(7)
# print(test.getHead().getValue())
# test.remove(6)
# print(test.getHead().next.getValue())
# print(test.indexOf(5))
# print(test.indexOf(7))
# test.removeIndex(1)
# print(test.getHead().next.getValue())
print(test.reverse())
