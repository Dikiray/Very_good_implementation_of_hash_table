class ListIterator():
    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    def __next__(self):
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1
        return self._collection[self._cursor]


class hash_table():
    def __init__(self):
        self.__spis = [[] for i in range(1000001)]
        self.__len = 1000000
        self.__col = 0
        self.__ilem = []

    def __contains__(self, x):
        r = hash(x) % self.__len
        return x in self.__spis[r]

    def __len__(self):
        return self.__col

    def __iter__(self):
        return ListIterator(self.__ilem, -1)

    def add(self, x):
        r = hash(x) % self.__len
        if(x not in self.__spis[r]):
            self.__spis[r].append(x)
            self.__ilem.append(x)
            self.__col += 1

    def remove(self, x):
        r = hash(x) % self.__len
        if(x in self.__spis[r]):
            self.__spis[r].remove(x)
            self.__ilem.remove(x)
            self.__col -= 1

d = hash_table()
d.add("Hellow")
d.add("Hellow2")
d.add("Hellow3")
for item in d:
    print(item)
print(len(d))
d.remove("Hellow")
