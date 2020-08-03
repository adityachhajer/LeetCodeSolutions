class MyHashSet:

    def __init__(self):
        self.l = []

    def add(self, key: int) -> None:
        self.l.append(key)

    def remove(self, key: int) -> None:
        self.l = [i for i in self.l if i != key]

    def contains(self, key: int) -> bool:
        if key in self.l:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)