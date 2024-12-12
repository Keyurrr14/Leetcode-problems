class MyHashSet:

    def __init__(self):
        self.arr = set()
        

    def add(self, key: int) -> None:
        self.arr.update({key})
        

    def remove(self, key: int) -> None:
        if key in self.arr:
            self.arr.remove(key)
            return True

    def contains(self, key: int) -> bool:
        return key in self.arr
        