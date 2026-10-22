class MyHashSet:

    def __init__(self):
        self.hash = [[], [], [], [], [], [], [], [], [], []]

    def add(self, key: int) -> None:
        index = key % 10
        if key not in self.hash[index]:
            self.hash[index].append(key)
        else:
            pass
        return

    def remove(self, key: int) -> None:
        index = key % 10
        if key in self.hash[index]:
            self.hash[index].remove(key)
        else:
            pass
        return

    def contains(self, key: int) -> bool:
        
        index = key % 10
        if key in self.hash[index]:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)