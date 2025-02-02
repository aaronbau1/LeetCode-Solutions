class MyHashSet:

    def __init__(self):
        self.keys = []

    def add(self, key: int) -> None:
        if not (key in self.keys):
            self.keys.append(key)

    def remove(self, key: int) -> None:
        if key in self.keys:
            self.keys.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.keys:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)