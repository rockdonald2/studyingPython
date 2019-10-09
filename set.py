class CustomSet:
    def __init__(self):
        self.collection = list()

    def has(self, value):
        try:
            return self.collection.index(value) >= 0
        except ValueError as ve:
            return False

    def values(self):
        return self.collection

    def add(self, value):
        if self.has(value):
            return False
        else:
            self.collection.insert(len(self.collection), value)
            return True

    def remove(self, value):
        if self.has(value):
            self.collection.remove(value)
            return True
        else:
            return False

    def size(self):
        return len(self.collection)

    def union(self, unionmember):
        if isinstance(unionmember, CustomSet):
            unionSet = CustomSet()

            for x in range(0, self.size()):
                unionSet.add(self.values()[x])

            for x in range(0, unionmember.size()):
                unionSet.add(unionmember.values()[x])

            return unionSet
        else:
            return self

    def intersection(self, intermember):
        if isinstance(intermember, CustomSet):
            interSet = CustomSet()
            for x in range(0, self.size()):
                if intermember.has(self.values()[x]):
                    interSet.add(self.values()[x])

            return interSet
        else:
            return self

    def difference(self, diffMember):
        if isinstance(diffMember, CustomSet):
            diffSet = CustomSet()
            for x in range(0, self.size()):
                if not diffMember.has(self.values()[x]):
                    diffSet.add(self.values()[x])

            return diffSet
        else:
            return self

    def subset(self, setMember):
        if isinstance(setMember, CustomSet):
            hash = CustomSet()

            for x in range(0, self.size()):
                if setMember.has(self.values()[x]):
                    hash.add(self.values()[x])

            if hash.size() ==  self.size():
                return True
            else:
                return False
        else:
            return False

test = CustomSet()
test2 = CustomSet()
test.add(5)
test.add(6)
test.add(5)
test.add(7)
test.add(1)
test2.add(1)
test2.add(10)
test2.add(20)
test.remove(5)
print(test.values())
print(test.size())
print(test2.values())
print(test.union(test2).values())
print(test.intersection(test2).values())
print(test.difference(test2).values())
print(test.subset(test2))
